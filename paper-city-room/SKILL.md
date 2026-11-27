---
name: paper-city-room
description: Draw a "room" for Paper City - one hand-drawn city block in pencil and wax crayon (a landmark with its people and traffic) that plays live beside the chat as an interactive HTML preview. It is written as one JavaScript file (room.js) and drawn by the real Paper City engine, with no image or video model. Use whenever the user mentions Paper City or a Paper City room, asks for a place (a landmark, a street, a city, their hometown) as a hand-drawn pencil-and-crayon city block, or asks to change a room already made.
---

# Drawing a Paper City room

Paper City is a city drawn in pencil and wax crayon, live in the browser. The city is a grid of square 24 m
blocks called **rooms**. Each room is one place (a temple, a market, an observatory) with its people, animals and
traffic, and each is a single file, `room.js`, built from a kit of shapes and ready-made parts.

**You write one file, `room.js`.** `build.py` (in this skill) checks it, pastes it into `viewer.html` and zips the
result, and that zip plays beside the chat: the room drawn by the real Paper City engine, moving, which the user
can drag, zoom and tap.

## In a chat

The user usually says very little: a place ("Sagrada Família"), a city ("Lisbon"), or a kind of place ("a ramen
street at lunchtime", "my grandmother's farm"). That is enough. **Do not ask questions first; draw.** The one
exception is a chat with no place in it at all (below).

- **The place is the one the user wrote in their prompt:** on a template's `Place:` line, or anywhere else in
  their message or its notes. The template's name and its example picture are never the place.
- **No place yet:** a template's `Place:` line still blank or still showing its `____`, and no place anywhere
  else. Don't start and don't fetch anything. Ask in one short line which place to draw, with three quick ideas
  of different kinds (a landmark, a busy street or market, somewhere of their own), and stop there. When they
  answer, that is the place: draw it at once, with no more questions.
- **A landmark:** draw it. **A city only:** pick the one place everyone knows it by. **A kind of place or an
  invented one:** design it; choose a landmark for it (the tallest, oddest or best-loved thing there).
- **Before you start, say in one or two lines what you will draw:** the landmark, the ground, and two or three
  bits of street life ("Galata Tower at the back with its cone roof, a cobbled square, a simit cart, a tram,
  cats"). Then work through the steps below without stopping to ask.
- **A change** ("more people", "make the tower taller", "add a fountain"): edit the same `room.js`, run
  `build.py` again with the same id, and deliver the new zip. **Another place:** a new `room.js` and a new id;
  each room is its own preview.
- **What a room cannot be:** night or weather, an interior, a photo-real picture, another art style, sound. Say so in
  one line and draw the nearest thing that it can be (lanterns and lit signs for an evening; the building from
  outside for an interior).
- Keep your words short. The user came for the picture, not for a report on how it was made.

## 0. Get this skill's files

This skill is a folder: `SKILL.md`, `build.py`, `viewer.html` (2 MB: the engine), `references/` and `images/`.
**A skill installed from GitHub (fal Agent's Skills page) brings only the markdown,** so first look for
`viewer.html` and `build.py` beside this file. If either is missing, fetch the whole folder into your workspace:

```sh
git clone --depth 1 https://github.com/kevintngo/paper-city-skill && cd paper-city-skill/paper-city-room && ls
```

Without git: `curl -L -o skill.zip https://github.com/kevintngo/paper-city-skill/archive/refs/heads/main.zip`
and unzip it (the folder is `paper-city-skill-main/paper-city-room`). If the skill came as a zip, unzip that
instead. Every path below is inside that folder. Do not go on without `viewer.html`: it cannot be written from
memory, and a room drawn any other way is not a Paper City room.

## How it looks

Paper City looks **drawn by hand**, as if someone sketched it on a sheet of cream paper: wobbly pencil outlines on
every edge, wax crayon filling the faces with visible strokes and gaps, the paper's grain showing through, a few
soft colors, a toy-like view from above at an angle. No smooth shading, no gradients, no cast shadows, no flat
digital color, no clean vector lines. `images/good-griffith-close.jpg` shows it up close.

**All of that comes from the engine inside `viewer.html`, never from you.** You only describe shapes with the kit
(`block`, `cyl`, `dome`, `tree`, `person` ...); the engine draws them in pencil and crayon. So never write a
renderer, a three.js scene, an SVG, a canvas drawing or a mockup of your own, and never use an image, video or
3D model to make the room: anything made that way looks digital and wrong, and costs the user money. This
whole job is writing one text file and running one script.

## 1. Look at the pictures

In `images/`, before writing anything:

- `good-griffith-whole.jpg`: **the target.** One landmark (the observatory) big at the back, a lawn and a drive in
  front, 15 people, 3 cars, palms, a sign. Its code: `references/example-griffith.md`.
- `good-griffith-close.jpg`, `good-griffith-phone.jpg`: up close, and as small as on a phone (what can't be read
  at that size is too small).
- `good-asakusa-whole.jpg`: a denser room: a pagoda and a hall at the back, stalls and a pond in front.
- `city-example.jpg`: nine rooms with streets between them. `parts.jpg`: every ready-made part.
- `bad-tall-near-corner.jpg`: **mistake.** A tower at the near corner hides the whole room.
- `bad-windows-inside-wall.jpg`: **mistake.** A blank house: its windows were laid inside the block, not on its
  front wall. `template-close.jpg` is the same house done right.

## 2. Read

- `references/api.md`: the whole API on one page. Read it in full.
- `references/recipes.md`: **how to draw the usual things**, as snippets that work as written: a building with
  windows on its visible walls, a tower and spire, a dome, a minaret, gables and arches, lawns and water, a drive
  with cars, a market, a café, people, things that move, trees, signs. Start from these.
- `references/example-griffith.md`, `references/example-istanbul.md`: two finished rooms, start to end.
- `references/example-parts.md`: every ready-made part called once. `references/parts.md`: every part with all
  its options and their defaults.

## 3. Plan

- **Space.** x runs right-and-down on screen, z left-and-down, y up. The room spans -12..12 on x and z.
- **Only faces toward +x and +z are seen.** The far edges are -x and -z: the landmark and anything tall go there.
  Keep the near corner (+12, +12) low, or it hides the room.
- **One landmark first,** the thing that makes the place itself, drawn with the kit, big and observed with care:
  its real shape, proportions, colors and the details people know it by. Toy scale: a 14 to 19 m tower is fine,
  a person is 1.8 m, a story 3 m.
- **Then the ground** (roads, lawns, paths, water), **then street life:** 12 to 18 people doing what people do
  there, and 4 to 10 things that move (walkers, traffic, flags, fountains, boats).
- **Write down the footprint of everything before writing code:** buildings, road rings, stalls, seating, as x
  and z ranges. Two things in one spot is the commonest mistake.
- **White card and a few crayons:** one or two main colors with small bright accents. Use the style families
  (`plain_<color>`, `bricks_<color>`, `tiles_<color>`, `round_<color>`, `flat_<color>`, `crown_<color>`).

## 4. Write room.js

One file, 100 to 200 lines, shaped like the examples:

```js
// <Place>, <city>: one line on what is drawn.
import { block, cyl, flatsY, rect, person, dog, traffic, oval } from '../../src/kit.js';
import { windows, door, roof, dome, tree, bench, lamp, flag, road, sign } from '../../src/parts.js';

const FRONT = -6;                                   // constants shared by several calls go up here
const DRIVE = oval(1, 3, 7, 5, { n: 40, exp: 0.55 });

export default {
  icon: 'M4 20h16M6 20V10l6-5 6 5v10',             // the room's button: one SVG path on a 24 x 24 grid
  slab: 'paving',                                   // the floor
  model() {                                         // never async
    // the landmark, at the back
    // the ground
    // street life: people, things that move
  },
};
```

Import exactly the names you use, from `../../src/kit.js`, `../../src/parts.js` and, for a style of your own,
`../../src/styles.js`. Nothing else can be imported. (The paths stay as written wherever you save the file.)

## 5. Check it line by line

Go through `room.js` against this list before building. `build.py` catches wrong imports and repeated names; it
cannot see where things stand.

- Every wall that carries `windows` or a `door` uses the wall's own coordinate: on `block(n, x0, x1, y0, y1, z0, z1)`
  the +z face is at `z1` and the +x face at `x1`, so `windows('z', z1, ...)`, never the block's middle.
- Nothing tall at the near corner; the landmark at the back.
- No two footprints overlap: compare each building, stall, bench and lawn with your footprint list.
- No stall, seat or standing person on a road: work out each road's outer edge (its points plus half its width).
  Walkers' routes don't cross the room's own traffic.
- A closed route is under three quarters full: vehicle lengths plus gaps (a car about 5.3 m, a motorbike 2.9 m)
  against the route's length.
- Every option has the same kind of value as its default in `references/parts.md`: a list stays a list
  (`stall(at, { awning: ['red', 'card'] })`; `awning: 'red'` breaks the whole room).
- Every route for `traffic` is points `[x, y, z]` (three numbers each), as `oval(...)` gives.
- Lettering fits: about `0.62 * h` per letter. Latin letters with accents work (`É`, `Ü`, `Ş`, `Ç`, `Ğ`, `İ`, `Ñ`,
  `Å` ...); other scripts (Greek, Cyrillic, Arabic, Chinese ...) don't: write the name in Latin letters.
- Every `dyn_` group, `person`, `dog` and `cat` has a name no other one in the room uses.
- Everything inside -12..12; every name you call exists in `references/api.md` or `references/parts.md`.

## 6. Build the preview

```sh
python3 <this skill's folder>/build.py room.js <id> --shot      # <id>: a short lowercase name, e.g. galata
```

It prints a line starting with `!` for each thing wrong in `room.js` (a name that is not imported, an import
that does not exist, two people with one name): fix them all and run it again. When it finds nothing it writes,
in `out/` beside `room.js`:

- `out/<id>/index.html`: the preview, one self-contained file (about 2 MB) that needs no server and no network.
- `out/<id>.zip`: `index.html` and `room.js` at its top level. **This is what you deliver.**
- `out/<id>.png` with `--shot`, when this machine has Playwright and a browser: a picture of the page after it
  has drawn. If it says there is no browser, carry on without the picture.

**Look at the picture if there is one.** Compare it with `images/good-griffith-whole.jpg`: is the landmark the
place at a glance, are windows on the walls, is anything standing in a road or inside something else, is the
near corner low, are there people and things moving? If something in `room.js` breaks while drawing, the page
says so in a red box at the bottom (for example `room.js: awning.map is not a function`) and `build.py` prints
it. Fix `room.js`, build again; two rounds are usually enough. Stop when the room reads at a glance.

Change nothing in `viewer.html` and do not make `index.html` any other way: the page is made to run inside a
locked-down preview frame (inline scripts only, no network). Do not split it into files, load anything from a
CDN, or rewrite it. (Without Python: `index.html` is `viewer.html` with the text `// PUT room.js HERE` replaced
by `room.js`, and the zip is those two files with no folder around them.)

## 7. Hand it back, so the room shows beside the chat

The user wants to **see the live, hand-drawn room next to the conversation**, not to download something.

1. **Deliver `out/<id>.zip` as the result, once,** after your last build and in the same turn, so it is not
   lost if the workspace is reset. Do not deliver an early build and then a better one: each delivered zip opens
   its own preview, and a second one stops the first. In fal Agent a zip with an `index.html` at its top level
   gets an **Open preview** button, and **Run preview** then plays it in the panel to the right of the chat.
2. **Say in one line how to see it:** "Press **Open preview** on the file, then **Run preview**: the room plays on
   the right. Drag to move around, scroll to zoom." The panel may say some resources are blocked; the room draws all
   the same.
3. If there is a picture, show it too, as a still of the same room.
4. **End with two or three things the user could ask for next,** in their words, not yours: a change to this room
   ("more people at the café", "a taller tower", "a market in front") or another place from the same city.

Then stop. Do not explain the code, list the files, or describe the steps you took. Do not answer with a 3D
scene, a generated image or a video in place of the preview: those are not the engine's drawing.

**Only if the user asks how to keep the room in their own Paper City project:** `room.js` goes in as
`rooms/<id>/room.js`, with one line in `world.json`:
`{ "id": "<id>", "cell": [c, r], "height": <tallest thing in m> }`. If the map still holds only the starter room
`_template`, the new room takes its place and becomes `home`. Streets in `streets` run along the gaps between
cells; extend them to reach a new cell.
