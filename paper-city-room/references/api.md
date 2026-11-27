# The room API

Everything a room file can call: shapes from `src/kit.js`, ready-made parts from `src/parts.js`, styles, people, motion and traffic.

## The file

```js
import { block, person } from '../../src/kit.js';
import { tree, roof, windows, flag } from '../../src/parts.js';

export default {
  icon: 'M4 20h16M6 20V10l6-5 6 5v10',        // the dock button: one SVG path on a 24 x 24 grid
  slab: 'paving',                              // the style of the floor (left out: bare card)
  model() {                                    // the shapes; it must not be async
    block('hall', -9, -3, 0, 4, -10, -6, 'bricks_clay');
    roof('hip', -9, -3, -10, -6, 4, { m: 'tiles_ink' });
    windows('z', -6, -9, -3, { n: 4, y: 1.2, h: 1.6, shape: 'arch', frame: 'card' });
    flag([0, 0, -9], { bands: ['red', 'card'] });
    tree([6, 0, -8]);
    person('guide', [2, 0, 3], 'wave', { rot: -45 });
  },
  // optional: build(room, world) for motion of your own, ground(x, z) for a floor that is not flat,
  // paths: { name: [[x, y, z], ...] } for walkers, cast(room, people) to hand people things
};
```

## Space and scale

- **x runs right-and-down on screen, z left-and-down, y up.** The room is 24 m square: x and z from -12 to 12.
- The far edges are -x and -z, the near corner is (+12, +12). **Tall things at the back, the near half low.**
- Only walls that face +x or +z are seen. `rot` turns a thing counterclockwise seen from above (+x toward -z).
- Toy scale: a person 1.8 m, a door 2.2 m, a story 3 m, a car 4 m; a landmark is squeezed to fit (a 14 m tower).

## Shapes (`src/kit.js`)

Each takes a name, what it is, where, a style `m`, and options (`rot`, `parent` ...); each gives back the object.

| | |
| --- | --- |
| `block(name, x0, x1, y0, y1, z0, z1, m)` | a box by its extents (`taper: [tx, tz]` narrows the top) |
| `box(name, [sx, sy, sz], at, m)` | a box by size, standing on `at` |
| `cyl(name, r, h, at, m, { segs, r2 })` | a cylinder; `r2: 0` a cone; `segs: 8, smooth: false` a faceted post |
| `sphere(name, r, at, m, { squash })`, `balls(name, centers, r, m)` | a ball; many balls as one object |
| `extrude(name, [[x, z], ...], y0, h, m, { top })` | a plan raised into a prism (islands, pools, odd footprints) |
| `profile(name, [[a, y], ...], depth, at, m, { axis })` | an elevation pushed sideways (gables, hulls, arches) |
| `lathe(name, [[r, y], ...], at, m)` | a turned shape (vases, domes, bells, statues) |
| `quad`, `mesh`, `terrain(name, nx, nz, x0, x1, z0, z1, (x, z) => y, m)` | one face; a raw mesh; ground that is not flat |
| `wire(name, points, m)`, `strokes(name, lines, m)` | hand-drawn lines (cables, railings, mullions) |
| `flatsX(name, x, outlines, m)`, `flatsZ`, `flatsY` | flat shapes on a wall facing +x or +z, or on the ground |
| `rect`, `arch`, `lancet`, `disc`, `star` | outlines for the flats |
| `text(name, 'WORDS', at, { h, face, m })` | lettering; accents work (`'CAFÉ'`, `'BƯU ĐIỆN'`); `flat: true` on the ground |
| `group('dyn_name', at, { behave })` | things parented to it (`parent: g`) move with it |
| `person(name, at, action, { rot, ... })`, `dog`, `cat` | the cast |
| `traffic(points, { vehicles, speed, oneWay })` | vehicles on a route inside the room |
| `tilt`, `paint`, `join`, `catenary`, `oval` | change a shape; points for cables and round routes |

## Parts (`src/parts.js`)

(`images/parts.jpg` shows every part.)

A part stands on `at` and needs no name.

- **Buildings:** `windows(axis, plane, from, to, { n, rows, w, shape, frame, split })` (a whole face of openings),
  `door`, `roof(kind, x0, x1, z0, z1, y)` with kind `gable`, `hip`, `pyramid`, `shed`, `mansard`, `flat`; `spire`,
  `dome`, `columns(a, b)`, `bands` (cornices, string courses), `steps`, `awning`, `board(at, 'WORDS')`.
- **Green:** `tree(at, { kind })` with kind `round`, `cone`, `column`, `palm`; `bush`, `hedge(a, b)`, `flowers`, `planter`.
- **Street:** `bench`, `lamp`, `sign(at, 'WORDS')`, `stall`, `cart`, `seats` (a table and stools; it gives back where
  to sit), `parasol`, `fence(points)`, `powerline(points)`, `lanterns(a, b)`, `bicycle`.
- **Moving by themselves:** `flag(at, { bands, emblem })`, `clock`, `bell`, `fountain`.
- **Ground:** `road(points, { closed })`, `zebra`; lawns, water and paths are `flatsY(..., 'lawn' | 'water' | 'gravel')`.

Parts are shortcuts, never limits: each is a few kit calls, takes its styles as options and gives back what it
made. The landmark that makes the place itself is usually drawn with the kit.

## Styles

- White things: `card`, `concrete`, `stone`, `glass`, `window` (dark glass), `shadow` (a dark opening).
- One crayon with a few marks: `clay`, `rust`, `kraft`, `oat`, `wood`, `olive`, `moss`, `sage`, `sky`, `bay`, `mist`,
  `fig`, `blush`, `mustard`, `butter`, `heather`, `brick`, `red`, `jade`, `ink`, `graphite`, `grass`, `leaf`, `aqua`.
- **A family and any of those colors**, no entry needed: `plain_jade` (no marks), `flat_chalk` (no outline, no
  shading: stripes, dials, markings), `round_red` (balls, balloons, flowers), `bricks_clay`, `tiles_ink` (roofs),
  `planks_wood`, `crown_blush` (a tree in that color). A third word picks the outline: `plain_butter_mustard`.
- Ground: `paving`, `lawn`, `gravel`, `road`, `curb`, `sand`, `rock`, `hill`, `water`, `foliage`, `trunk`.
- Lines: `pencil`, `pencil_thin`, `iron`, `cable`, `chalk`, `dash_chalk`, `crayon_<color>[_thin|_thick]`.
- Anything else: `registerStyles({ myroom_thing: colored('butter', 'rust') })` from `src/styles.js`.

## People, motion, traffic

- **Actions:** `stand`, `talk`, `wave`, `sit` (`h`: seat height), `sit_ground`, `lie`, `type`, `dance`, `photo`,
  `taichi`, `drum`, `cheer`, `point`, `water`, `fish`, `throw`/`catch`; travelers `walk`, `jog`, `skate`, `carry`
  take `to: [x, y, z]` (there and back) or `path: 'name'` with `loop: 1`. 12 to 18 people a room.
- **Clothes** when the place calls for them: `top`, `bottom`, `hat`, `hair`, `skin` (colors), `topKind`, `bottomKind`
  (`gown`, `skirt` ...), `hairStyle` (`bun`, `cap`, `helmet`, `nonla` ...). `holds: 'name'` carries the `dyn_name` group.
- **Motion with no script:** `group('dyn_x', at, { behave })` with `flag`, `sway`, `bell`, `clock`, `spin`, `bob`
  (floats), `pulse` (fountain jets), `shuttle` (`to: [x, y, z]`: a ferry, a tram), `orbit` (`radius`); options in
  `src/behaviors.js`. Four to ten things that move make a room alive.
- **Vehicles:** `car_sky`, `car_mustard`, `car_fig`, `car_sage`, `car_clay`, `taxi`, `taxi_mustard`, `truck_card`,
  `bus_clay`, `bus_sky`, `tram`, `cablecar`, `bike_clay`, `bike_sky`, `bike_mustard`, `moto_red` (and `_sky`,
  `_mustard`, `_jade`, `_fig`, `_card`, `_boxes`), `cyclo`. A new one is a few kit calls in `assets/models/vehicles.js`.

## Taste

1. **Recognizable at a glance, on a phone.** One landmark, observed with care, big; everything else supports it.
2. **White card and a few crayons.** One or two dominant colors and small bright accents.
3. **Model the edges you want drawn and no more.** Every hard edge gets a pencil line; tiny details turn to clutter.
4. **Flat things sit proud.** The flats do it by themselves; anything else laid on a face needs a millimeter.
5. **Leave room for life:** benches, stalls, paths, a few things that move.
