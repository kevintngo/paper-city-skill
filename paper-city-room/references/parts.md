# Every ready-made part, with its options

From `src/parts.js`. Each stands on `at` ([x, y, z]), needs no name, takes options in `o` and gives back what it
made. **Give each option the same kind of value as its default:** a list where the default is a list
(`awning: ['red', 'card']`, never `awning: 'red'`), a color name where it is a color name, a style where it is a
style. Leave out what you do not need. "also" lists options read without a default.

```js
/** A sheet between two edges, a -> b and d -> c, cut into `n` bands of alternating styles: awnings, parasols,
 *  striped flags, a barber's pole laid flat. Seen from both sides. */
export function striped(name, a, b, c, d, n, mats, o = {})

/** A tree. `kind`: 'round' (a trunk and a few balls), 'cone' (a fir), 'column' (a cypress, a poplar) or 'palm'.
 *  `h` is the height of the trunk, `r` the radius of the crown, `m` its style (`foliage`, or `crown_<color>`). */
export function tree(at, o = {})
//   options, with their defaults: { kind = 'round', h = 3, r = 1.2, m = 'foliage', trunk = 'trunk' }

/** A bush: a low lump or two. */
export function bush(at, o = {})
//   options, with their defaults: { r = 0.6, m = 'foliage' }

/** A clipped hedge between two points on the ground. */
export function hedge(a, b, o = {})
//   options, with their defaults: { h = 0.9, w = 0.7, m = 'foliage' }

/** A bed of flowers: dots of color in a rectangle `w` by `d` centered on `at`. `colors` are palette names; the
 *  flowers of each color are one object. For any other layout, hand your own centers to balls(). */
export function flowers(at, o = {})
//   options, with their defaults: { w = 2, d = 1, colors = ['red', 'butter', 'blush', 'fig'], gap = 0.36, r = 0.15, rot = 0 }

/** A pot of flowers (or of anything: `fill` is the style of what grows in it). */
export function planter(at, o = {})
//   options, with their defaults: { r = 0.42, m = 'stone', colors = ['red', 'blush', 'butter'] }
//   also: fill

/** A bench, `w` long. Someone sitting on it: person(name, at, 'sit', { rot, h: 0.45 }) with the bench's own `rot`. */
export function bench(at, o = {})
//   options, with their defaults: { rot = 0, w = 1.4, m = 'wood', legs = 'plain_graphite' }

/** A street lamp: a post `h` tall with a globe. `arm` meters of overhang hangs the globe out over the street. */
export function lamp(at, o = {})
//   options, with their defaults: { h = 3.2, post = 'plain_graphite', globe = 'round_butter', arm = 0, rot = 0 }

/** A board with words on it, centered on `at` and facing `face`: a shop sign on a wall, a name over a door.
 *  `size` is the height of the letters; the board fits the words unless `w` says otherwise. */
export function board(at, words, o = {})
//   options, with their defaults: { face = -90, size = 0.36, m = 'plain_butter', ink = 'crayon_rust' }
//   also: w, h, parent

/** The same board on two legs, standing on the ground at `at`. */
export function sign(at, words, o = {})
//   options, with their defaults: { rot = 0, size = 0.36, legs = 'wood' }
//   also: h, lift, w

/** A market stall: a counter under a striped awning on four posts, with a heap of goods. `awning` and `goods`
 *  are palette colors. */
export function stall(at, o = {})
//   options, with their defaults: { rot = 0, w = 2.2, d = 1.3, h = 2.1, awning = ['red', 'card'], counter = 'wood', goods = ['mustard', 'red', 'jade'] }

/** A pushcart: a body on two wheels with a glass case, a roof and a handle. Give it `words` for a board on top. */
export function cart(at, o = {})
//   options, with their defaults: { rot = 0, w = 1.6, body = 'card', roof = 'red', words = null }
//   also: size, ink

/** A low table with `n` stools round it. It gives back where to sit: [{ at, rot, h }, ...], ready for
 *  person(name, seat.at, 'sit', { rot: seat.rot, h: seat.h }). `stools` are styles, taken in turn. */
export function seats(at, o = {})
//   options, with their defaults: { n = 4, r = 0.8, h = 0.3, table = 'plain_sky', stools = ['plain_red', 'plain_sky'], turn = 30 }

/** A parasol: a pole and a canopy of `n` gores in alternating colors. */
export function parasol(at, o = {})
//   options, with their defaults: { r = 1.3, h = 2.3, colors = ['red', 'card'], n = 8 }

/** A railing or a fence along the points: a rail `h` up and a post every `every` meters. */
export function fence(points, o = {})
//   options, with their defaults: { h = 0.5, every = 1, m = 'iron', closed = false }

/** Poles with cables slung between them: `points` are [x, z] on the ground. `n` cables, each sagging a little
 *  more than the last; `tangle` adds that many loops of spare cable round each pole. */
export function powerline(points, o = {})
//   options, with their defaults: { h = 6, n = 4, sag = 0.8, pole = 'plain_stone_graphite', m = 'pencil_thin', tangle = 0 }

/** A string of lanterns (or of bunting, or of light bulbs) hanging from `a` to `b`. */
export function lanterns(a, b, o = {})
//   options, with their defaults: { n = 6, sag = 0.5, colors = ['red'], r = 0.16 }

/** A parked bicycle, facing +x until turned. It gives back its group: put a basket or a load on it. */
export function bicycle(at, o = {})
//   options, with their defaults: { rot = 0, color = 'jade' }

/** An awning over a shop front: `at` is the middle of its top edge on the wall, `face` the way the wall looks.
 *  It reaches `d` out and drops by `drop`, in stripes of the `colors`. */
export function awning(at, o = {})
//   options, with their defaults: { face = -90, w = 2.4, d = 0.9, drop = 0.35, colors = ['red', 'card'] }

/** A flag on a pole `h` tall. `bands` are palette colors from the top down (or from the pole out, with
 *  `vertical`); `emblem: { kind: 'disc' | 'star', color, r }` sits in the middle. It waves by itself, and gives
 *  back its cloth group (w wide along x, hgt tall, flat in z) for any other emblem you care to draw on it. */
export function flag(at, o = {})
//   options, with their defaults: { h = 3, w = 0.9, hgt = 0.6, bands = ['red'], vertical = false, emblem = null, rot = 0, pole = 'card' }
//   also: amp

/** A clock face of radius `r`, centered on `at` and facing `face`. It keeps time, and whirls when tapped. */
export function clock(at, o = {})
//   options, with their defaults: { face = -90, r = 0.6, dial = 'flat_chalk', hands = 'flat_graphite' }
//   also: time

/** A bell hung from `at`. It rings with the other bells of the room every half minute, and when tapped. */
export function bell(at, o = {})
//   options, with their defaults: { r = 0.36, m = 'round_mustard' }
//   also: every

/** A round fountain: a basin of radius `r` with water in it and `jets` jets that rise and fall (tap them). */
export function fountain(at, o = {})
//   options, with their defaults: { r = 1.6, m = 'stone', jets = 3 }

/** Rows of openings on a wall. `axis` 'x': the wall faces +x and stands at x = `plane`, and `from`..`to` run along
 *  z; `axis` 'z': it faces +z at z = `plane`, and they run along x (`back: true` for a wall facing the other way).
 *  `n` openings side by side, in each of `rows`: [[foot, height], ...] (a row may add its own shape as a third
 *  value). `shape`: 'rect', 'arch' or 'lancet'; `w` is the width of one. `frame` (a style) puts a rim round each,
 *  `split` a glazing bar down the middle. One call makes a whole face of windows, or one door. */
export function windows(axis, plane, from, to, o = {})
//   options, with their defaults: { n = 1, w = 0.6, shape = 'rect', m = 'window', frame = null, rim = 0.09, split = false, back = false }
//   also: rows, y, h, parent

/** One door on a wall: windows() with a single opening `w` wide and `h` tall, its foot at `y`, centered on `c`. */
export function door(axis, plane, c, o = {})
//   options, with their defaults: { w = 1, h = 2.2, y = 0, m = 'plain_wood_rust' }

/** A roof over the rectangle x0..x1, z0..z1 with its eaves at height `y`. `kind`: 'gable' (its ridge along the
 *  longer side unless `ridge` says 'x' or 'z'), 'hip', 'pyramid', 'shed' (`high`: the side that stands tall,
 *  '-x', '+x', '-z' or '+z'), 'mansard' (`taper: [tx, tz]` for the size of its flat top) or 'flat'. `h` is its
 *  height and `over` how far the eaves overhang. */
export function roof(kind, x0, x1, z0, z1, y, o = {})
//   options, with their defaults: { h = kind === 'flat' ? 0.25 : 1.5, m = 'tiles_clay', over = 0.2 }
//   also: ridge, high, taper

/** A spire: a short drum and a faceted cone of `segs` sides, with a cross `cross` meters tall on top (0: none). */
export function spire(at, o = {})
//   options, with their defaults: { r = 1, h = 6, segs = 8, m = 'tiles_ink', drum = 0.5, cross = 1 }

/** A dome of radius `r` (and height `h`, if it is not a half ball), with a small lantern on top unless `lantern: 0`. */
export function dome(at, o = {})
//   options, with their defaults: { r = 2, h = o.r ?? 2, m = 'plain_sage', segs = 16, lantern = 1 }

/** A row of `n` columns from `a` to `b` (points on the ground), each `h` tall on a square foot and under a square cap. */
export function columns(a, b, o = {})
//   options, with their defaults: { n = 6, h = 4, r = 0.25, m = 'card' }

/** Bands of trim round a block at the heights `ys`: string courses, a cornice, a plinth. Each stands `out`
 *  meters proud of the walls x0..x1, z0..z1 and is `h` tall. */
export function bands(x0, x1, z0, z1, ys, o = {})
//   options, with their defaults: { h = 0.22, out = 0.08, m = 'card' }

/** Steps up to a wall. `side` is the way they face ('+x', '-x', '+z' or '-z'), `edge` where the wall stands on
 *  that axis, and a0..a1 how far they run along it; `n` steps, each `rise` tall and `run` deep. */
export function steps(side, edge, a0, a1, o = {})
//   options, with their defaults: { n = 2, rise = 0.12, run = 0.36, m = 'stone', y = 0 }

/** A road `w` wide along the points ([x, z] or [x, y, z]; `closed` for a ring), with a dashed line down its
 *  middle unless `dash: null`. The same points make a route for traffic(). */
export function road(points, o = {})
//   options, with their defaults: { w = 2.2, m = 'road', closed = false, y = 0.012, dash = 'dash_chalk' }

/** A zebra crossing centered on `at`: `n` stripes, each `deep` long the way the traffic goes (which is +x until
 *  turned by `rot`), laid side by side over `across` meters of road. */
export function zebra(at, o = {})
//   options, with their defaults: { rot = 0, across = 2.2, deep = 2.2, n = 5, m = 'flat_chalk', y = 0.02 }
```
