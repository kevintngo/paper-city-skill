# Recipes: how to draw the usual things

Each snippet goes inside `model() { ... }` and was drawn by the engine as written. Change the numbers to fit
your room; keep the shape of the calls. The imports a snippet needs are listed above it.

The two rules behind most of them: **only faces toward +x and +z are seen**, so a building's front is its `z1`
(the +z face) and its side is its `x1` (the +x face); and **tall things go at the back** (-x, -z).

## A building, seen from its two visible sides

`block, windows, door, roof, bands, steps`

```js
// 8 m along x, 4 m deep, two stories (3.2 m each), at the back of the room
block('hall', -10, -2, 0, 6.4, -11, -7, 'bricks_clay');
bands(-10, -2, -11, -7, [3.1], { m: 'stone' });                        // a string course between the stories
roof('hip', -10, -2, -11, -7, 6.4, { h: 2, m: 'tiles_ink' });
// openings lie ON the walls that are seen: the +z face is at z = -7 (z1), the +x face at x = -2 (x1)
windows('z', -7, -9.6, -2.4, { n: 5, rows: [[0.9, 1.4], [4, 1.4]], frame: 'card' });   // rows: [foot, height]
windows('x', -2, -10.6, -7.4, { n: 3, rows: [[0.9, 1.4], [4, 1.4]], frame: 'card' });
door('z', -7, -6, { w: 1.4, h: 2.4 });                                 // on the +z wall, centered at x = -6
steps('+z', -7, -7, -5, { n: 3 });                                     // up to that door
```

## A tower with a spire, or a tower that narrows

`block, box, windows, spire, clock`

```js
block('tower', -11, -8, 0, 12, -11, -8, 'stone');
windows('z', -8, -11, -8, { n: 2, y: 7, h: 2.2, w: 0.5, shape: 'lancet', frame: 'card' });
clock([-9.5, 9.6, -7.98], { r: 0.9, face: -90 });                      // face -90: on a wall facing +z
spire([-9.5, 12, -9.5], { r: 1.9, h: 6, m: 'tiles_ink', cross: 0.8 });
box('obelisk', [1, 7, 1], [4, 0, -10], 'card', { taper: [0.5, 0.5] });  // taper: the top is half as wide
```

## A dome on a drum; a minaret

`cyl, dome`

```js
cyl('drum', 3, 1.4, [-4, 5, -8], 'card', { segs: 24 });                // on the roof of a 5 m block
dome([-4, 6.4, -8], { r: 3, h: 3.2, m: 'plain_sage_moss', segs: 24, lantern: 0 });
dome([-8, 5, -8], { r: 1.6, m: 'plain_sage_moss', lantern: 0, name: 'small_dome' });  // name it when there are several
// a minaret: a faceted foot, a shaft, a balcony, a pencil cap
cyl('min_foot', 0.6, 2, [3, 0, -11], 'card', { segs: 8, smooth: false });
cyl('min_shaft', 0.35, 10, [3, 2, -11], 'card', { segs: 12 });
cyl('min_balcony', 0.6, 0.25, [3, 9, -11], 'card', { segs: 12 });
cyl('min_cap', 0.4, 2.4, [3, 12, -11], 'plain_mist_graphite', { segs: 12, r2: 0 });   // r2: 0 is a cone
```

## Odd shapes: a gable, an arch, a hull, a turned statue

`profile, extrude, lathe, arch`

```js
// a gable end: an outline in x-y, pushed 6 m along z
profile('gable', [[-3, 0], [3, 0], [3, 3], [0, 5], [-3, 3]], 6, [6, 0, -9], 'plain_butter', { axis: 'z' });
// a gateway: two posts and a beam, with an arched opening drawn on its front
block('gate', -1.5, 1.5, 0, 4, 3, 3.8, 'plain_red');
flatsZ('gate_hole', 3.8, [arch(0, 0, 1.8, 3)], 'shadow');              // a dark round-headed opening on the +z face
// a plan raised into a prism: an L-shaped terrace 0.6 m high
extrude('terrace', [[-11, 5], [-5, 5], [-5, 8], [-8, 8], [-8, 11], [-11, 11]], 0, 0.6, 'stone');
// a statue on a plinth: a turned outline [radius, y]
box('plinth', [1.2, 1, 1.2], [8, 0, 3], 'stone');
lathe('statue', [[0.35, 0], [0.4, 0.6], [0.25, 1.3], [0.32, 1.6], [0.18, 1.9], [0, 2.1]], [8, 1, 3], 'plain_jade');
```

## Ground: lawn, water, a path, a hill

`flatsY, rect, disc, terrain`

```js
flatsY('lawn', 0.01, [rect(2, 11, -11, -4)], 'lawn');                  // rect(x0, x1, z0, z1)
flatsY('pond', 0.02, [disc(6, -7, 2, 24)], 'water');                   // disc(x, z, r, n)
flatsY('path', 0.015, [rect(-1, 1, -4, 12)], 'gravel');
// a hill rising toward the back corner
terrain('hill', 12, 12, -12, -4, -12, -4, (x, z) => Math.max(0, (-4 - x) * (-4 - z)) * 0.03, 'hill');
```

## A drive round a lawn, with cars on it

`oval, road, traffic`

```js
const DRIVE = oval(2, 3, 7, 5, { n: 40, exp: 0.55 });                  // put this line above export default
road(DRIVE, { closed: true, w: 2 });
traffic(DRIVE, { vehicles: ['car_sky', 'taxi', 'bike_mustard'], speed: 2.2, size: 0.9 });
// a closed route stays under 3/4 full: here about 40 m long, cars 5.3 m and a bike 2.9 m with their gaps
```

## A market, a café, a bench

`stall, lanterns, parasol, seats, bench, person`

```js
stall([-6, 0, 8], { rot: 0, awning: ['red', 'card'], goods: ['mustard', 'red', 'jade'] });   // lists, not one color
stall([-3, 0, 8], { awning: ['jade', 'card'] });
lanterns([-8, 2.6, 6.6], [-1, 2.6, 6.6], { n: 7, colors: ['red', 'mustard'] });
person('seller', [-6, 0, 9.2], 'talk', { rot: 90 });
// a table with four stools, and people on them
parasol([4, 0, 8], { n: 8 });
const cafe = seats([4, 0, 8], { n: 4 });
cafe.forEach((s, i) => person(`coffee${i}`, s.at, 'sit', { rot: s.rot, h: s.h }));
bench([9, 0, 5], { rot: -90 });
person('reader', [9, 0, 5], 'sit', { rot: -90, h: 0.45 });             // same spot and rot as the bench
```

## People, a dog, a cat

`person, dog, cat`

```js
person('guide', [0, 0, 1], 'wave', { rot: -45, top: 'sky', hat: 'mustard' });
person('tourist', [1, 0, 1.6], 'photo', { rot: 135 });
person('walker', [-10, 0, 11], 'walk', { to: [10, 0, 11] });           // walks there and back
person('jogger', [11, 0, -10], 'jog', { to: [11, 0, 10], top: 'red' });
person('picnic', [5, 0, -6], 'sit_ground', { rot: 30 });
person('nun', [-2, 0, 2], 'stand', { topKind: 'gown', top: 'ink', hairStyle: 'bun' });
dog('rex', [2, 0, 4], 'run_circle', { radius: 1.5 });
cat('tom', [-4, 0, -6.7], 'sit');                                       // every name is used once
```

## Things that move by themselves

`flag, fountain, group, box, sphere, cyl`

```js
flag([10, 0, -2], { bands: ['red', 'card', 'bay'] });                  // it waves
fountain([0, 0, -2], { r: 1.4, jets: 4 });                             // its jets rise and fall
// a boat that bobs on the pond: parts parented to a dyn_ group move with it
const boat = group('dyn_boat', [6, 0.05, -7], { behave: 'bob' });
box('boat_hull', [1.6, 0.35, 0.7], [0, 0, 0], 'plain_wood', { parent: boat });
// a ferry that shuttles from one point to another and back
const ferry = group('dyn_ferry', [-10, 0.05, 2], { behave: 'shuttle', to: [-10, 0.05, 10] });
box('ferry_hull', [1.6, 0.5, 3.2], [0, 0, 0], 'plain_card', { parent: ferry });
// a sign that turns, a lantern that sways
const turner = group('dyn_turner', [8, 3, 9], { behave: 'spin', speed: 0.5 });
box('turner_board', [0.1, 0.8, 1.4], [0, 0, 0], 'plain_mustard', { parent: turner });
const swing = group('dyn_swing', [-9, 2.4, 4], { behave: 'sway', amp: 0.25 });
sphere('swing_lamp', 0.25, [0, -0.3, 0], 'round_red', { parent: swing });
```

## Trees, bushes, flowers, lamps

`tree, bush, hedge, flowers, lamp`

```js
tree([-11, 0, 0], { kind: 'round', h: 2.5, r: 1.4 });
tree([11, 0, -11], { kind: 'cone', h: 5 });
tree([11, 0, -6], { kind: 'column', h: 4.5, r: 0.7 });                 // a cypress
tree([-11, 0, 6], { kind: 'palm', h: 5.5, r: 1.4 });
tree([0, 0, 10], { m: 'crown_blush' });                                // a cherry in bloom
bush([3, 0, -3], { r: 0.6 });
hedge([-6, 0, -3], [-1, 0, -3]);
flowers([7, 0, -9], { w: 4, d: 1.5, colors: ['red', 'mustard', 'blush'] });
lamp([6, 0, 10]);
```

## Words: a sign, a board on a wall, letters on the ground

`sign, board, text`

```js
sign([10.5, 0, 10.5], 'MARKET', { rot: -45, size: 0.4 });              // on two legs
board([-6, 5.2, -6.94], 'TOWN HALL', { face: -90, size: 0.45 });      // on the +z wall at z = -7
text('painted', 'BUS', [0, 0.02, 6], { h: 0.8, flat: true, m: 'chalk' });
// about 0.62 * h per letter: 'TOWN HALL' at size 0.45 is about 2.5 m wide
```

## A color of your own (only when the families can't do it)

`registerStyles, colored` from `../../src/styles.js`

```js
// at the top of the file, after the imports
registerStyles({ myroom_terracotta: colored('clay', 'rust') });
// then use 'myroom_terracotta' as a style anywhere
```
