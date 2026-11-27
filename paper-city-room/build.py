#!/usr/bin/env python3
"""Checks a Paper City room and makes its preview: one command, standard library only.

    python3 build.py room.js <id>            ->  out/<id>/index.html, out/<id>/room.js, out/<id>.zip
    python3 build.py room.js <id> --shot     ->  also out/<id>.png, if this machine has Playwright and a browser

<id> is a short lowercase name for the place (galata, eiffel-tower). index.html is viewer.html (beside this
file) with room.js pasted in; the zip holds index.html and room.js at its top level, which is what a chat's
side panel plays. Lines that start with "!" are problems: fix them in room.js and run this again.
"""
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = '// PUT room.js HERE'
INTERNAL = {'begin', 'end', 'abort', 'uid', 'outline'}       # in kit.js, but not for rooms to call


def bare(src):
    """The source with its comments and the insides of its strings blanked out, every character still in its place."""
    def blank(m):
        t = m.group(0)
        inside = re.sub(r'[^\n]', ' ', t[1:-1] if t[0] in '\'"`' else t[2:])
        return t[0] + inside + t[0] if t[0] in '\'"`' else '  ' + inside
    return re.sub(r"'(?:\\.|[^'\\\n])*'|\"(?:\\.|[^\"\\\n])*\"|`(?:\\.|[^`\\])*`|//[^\n]*|/\*[\s\S]*?\*/", blank, src)


def line_of(src, pos):
    return src.count('\n', 0, pos) + 1


def check(src):
    """What is plainly wrong with room.js, as lines of text. An empty list: nothing found."""
    said = []
    names = json.load(open(os.path.join(HERE, 'references', 'names.json')))
    code = bare(src)

    if re.search(r'</script', src, re.I):
        said.append('room.js contains "</script": it cannot sit in the page. Remove it.')
    if not re.search(r'\bexport\s+default\b', code):
        said.append('no "export default { ... }": the room is the default export (see references/api.md).')
    if not re.search(r'\bmodel\s*(\(|:)', code):
        said.append('no model() in the default export: the shapes are made in model() { ... }.')
    if re.search(r'\basync\s+model\b|\bmodel\s*:\s*async\b', code):
        said.append('model() is async: it must not be. Make it a plain function.')

    # imports: only the kit's own modules, and only names they have
    imported = {}
    for m in re.finditer(r'\bimport\s*(?:([\w$]+)\s*,?\s*)?(?:\*\s*as\s+([\w$]+)|\{([^}]*)\})?\s*(?:from\s*)?(["\'])([^"\'\n]+)\4', src):
        default, star, braces, _, spec = m.groups()
        at = line_of(src, m.start())
        mod = re.fullmatch(r'\.\./\.\./src/(\w+)\.js', spec)
        if spec == 'three' or spec.startswith('three/addons/'):
            continue
        if not mod or mod.group(1) not in names:
            said.append(f'line {at}: imports "{spec}", which a room cannot import. Use ../../src/kit.js, '
                        '../../src/parts.js and ../../src/styles.js.')
            continue
        have = set(names[mod.group(1)])
        for part in (braces or '').split(','):
            part = part.strip()
            if not part:
                continue
            name, _, alias = part.partition(' as ')
            name, alias = name.strip(), (alias or name).strip()
            imported[alias] = mod.group(1)
            if name not in have:
                where = [k for k in ('kit', 'parts', 'styles') if name in names[k]]
                hint = f' It is in ../../src/{where[0]}.js.' if where else ' See references/api.md for what exists.'
                said.append(f'line {at}: "{name}" is not in {mod.group(1)}.js.{hint}')
        if star:
            imported[star] = mod.group(1)

    # called, but never imported or made here
    made = set(re.findall(r'\b(?:const|let|var|function|class)\s+([\w$]+)', code))
    for braces in re.findall(r'\b(?:const|let|var)\s*[\[{]([^\]}=]*)[\]}]\s*=', code):     # const { a, b } = ..., const [a, b] = ...
        made |= set(re.findall(r'[\w$]+', braces))
    known = (set(names['kit']) | set(names['parts'])) - INTERNAL
    for name in sorted(known):
        if name in imported or name in made:
            continue
        m = re.search(r'(?<![.\w$])' + re.escape(name) + r'\s*\((?![^)]*\)\s*\{)', code)
        if m:
            where = 'kit' if name in names['kit'] else 'parts'
            said.append(f'line {line_of(code, m.start())}: {name}() is used but not imported. '
                        f'Add it to the import from ../../src/{where}.js.')
    # two of the cast with one name
    for kind, pattern in (('person', r'\bperson\(\s*(["\'])([^"\'`]+)\1'), ('dog', r'\bdog\(\s*(["\'])([^"\'`]+)\1'),
                          ('cat', r'\bcat\(\s*(["\'])([^"\'`]+)\1'), ('group', r'\bgroup\(\s*(["\'])(dyn_[^"\'`]+)\1'),
                          ('marker', r'\bmarker\(\s*(["\'])([^"\'`]+)\1')):
        seen = {}
        for m in re.finditer(pattern, src):
            if code[m.start():m.start() + len(kind)] != kind:      # inside a comment or a string
                continue
            at = line_of(src, m.start())
            if m.group(2) in seen:
                said.append(f'line {at}: two {kind}s are named "{m.group(2)}" (the other is on line {seen[m.group(2)]}). '
                            'Give each its own name.')
            seen.setdefault(m.group(2), at)
    return said


def shoot(page_path, png):
    """A picture of the page as it draws, if this machine can take one. Returns what the page's red box says."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('no picture: Playwright is not installed here (pip install playwright && playwright install chromium). '
              'Go through the checklist in SKILL.md instead.')
        return None
    flags = ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--enable-webgl']
    with sync_playwright() as p:
        browser = None
        for how in ({}, {'channel': 'chrome'}):
            try:
                browser = p.chromium.launch(args=flags, **how)
                break
            except Exception:
                continue
        if not browser:
            print('no picture: no browser to open the page with (playwright install chromium).')
            return None
        page = browser.new_page(viewport={'width': 1000, 'height': 750})
        page.goto('file://' + page_path)
        try:
            page.wait_for_function("(window.__sheet && window.__sheet.ready) || document.getElementById('problems')", timeout=45000)
        except Exception:
            print('! the page did not finish drawing in 45 seconds.')
        page.wait_for_timeout(12000)
        box = page.query_selector('#problems')
        problems = box.inner_text() if box else ''
        page.screenshot(path=png)
        browser.close()
    print(f'picture: {png}  (look at it: compare with images/good-griffith-whole.jpg)')
    return problems


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 2
    room_path = args[0]
    rid = re.sub(r'[^a-z0-9]+', '-', (args[1] if len(args) > 1 else 'room').lower()).strip('-') or 'room'
    src = open(room_path, encoding='utf-8').read()

    problems = check(src)
    for line in problems:
        print('! ' + line)

    viewer = open(os.path.join(HERE, 'viewer.html'), encoding='utf-8').read()
    if MARK not in viewer:
        print('! viewer.html has no "' + MARK + '": use the viewer.html that came with this skill, unchanged.')
        return 1
    if '</script' in src.lower():
        return 1
    page = viewer.replace(MARK, src, 1).replace('data-id="room"', f'data-id="{rid}"', 1)

    out = os.path.join(os.path.dirname(os.path.abspath(room_path)), 'out')
    folder = os.path.join(out, rid)
    os.makedirs(folder, exist_ok=True)
    index = os.path.join(folder, 'index.html')
    open(index, 'w', encoding='utf-8').write(page)
    open(os.path.join(folder, 'room.js'), 'w', encoding='utf-8').write(src)
    zip_path = os.path.join(out, rid + '.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(index, 'index.html')
        z.write(os.path.join(folder, 'room.js'), 'room.js')

    if '--shot' in argv:
        drawn = shoot(index, os.path.join(out, rid + '.png'))
        if drawn:
            problems.append(drawn)
            print('! the page says: ' + drawn.strip()[:900])

    print(f'preview: {index}')
    if problems:
        print(f'{len(problems)} problem(s): fix every "!" line in room.js and run this again before delivering anything.')
    else:
        print(f'deliver: {zip_path}  ({os.path.getsize(zip_path) / 1e6:.1f} MB; index.html and room.js at its top level)')
        print('no problems found.')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
