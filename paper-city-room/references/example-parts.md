# A finished room: Every ready-made part

images/parts.jpg is how it draws. Each part called once, with its usual options.

```js
// Every ready-made part on one slab, each with its name written in front of it: a picture to choose from, and a
// worked example of how each is called. It is not on the map: see it with  node tools/room.mjs _parts
import { block, text, person, balls, group, sphere } from '../../src/kit.js';
import {
  tree, bush, hedge, flowers, planter, bench, lamp, board, sign, stall, cart, seats, parasol, fence, powerline, lanterns, bicycle, awning,
  flag, clock, bell, fountain, windows, door, roof, spire, dome, columns, bands, steps, road, zebra,
} from '../../src/parts.js';

const label = (words, x, z) => text('label_' + words.replace(/\W/g, ''), words, [x, 0.01, z], { h: 0.3, face: -90, flat: true, m: 'pencil_thin' });

export default {
  icon: 'M4 20h16M6 20V9l6-5 6 5v11M10 20v-5h4v5',
  slab: 'paving',
  model() {
    // --- buildings: a block, a roof on it, openings laid on its walls
    const house = (x, z, m, h = 2.6) => { block('house' + x, x - 1.4, x + 1.4, 0, h, z - 1.2, z + 1.2, m); return [x - 1.4, x + 1.4, z - 1.2, z + 1.2]; };
    let b = house(-10, -10, 'bricks_clay');
    roof('gable', ...b, 2.6, { m: 'tiles_ink', h: 1.3 });
    windows('z', b[3], b[0], b[1], { n: 3, y: 1.1, h: 1.0, w: 0.5, frame: 'card', split: true });
    door('x', b[1], -10, { frame: 'card' });
    label('GABLE', -10, -8.2);

    b = house(-6, -10, 'plain_butter_mustard');
    roof('hip', ...b, 2.6, { m: 'tiles_clay', h: 1.2 });
    windows('z', b[3], b[0], b[1], { n: 3, y: 0.7, h: 1.5, w: 0.5, shape: 'arch', m: 'plain_jade' });
    windows('x', b[1], b[2], b[3], { n: 2, y: 0.7, h: 1.5, w: 0.5, shape: 'arch', m: 'plain_jade' });
    label('HIP', -6, -8.2);

    b = house(-2, -10, 'bricks_brick', 3.4);
    roof('pyramid', ...b, 3.4, { m: 'tiles_ink', h: 1.8 });
    windows('z', b[3], b[0], b[1], { n: 3, w: 0.42, shape: 'lancet', m: 'plain_bay', rows: [[0.5, 1.2], [2.0, 1.1]] });
    label('PYRAMID', -2, -8.2);

    b = house(2, -10, 'card', 3.0);
    roof('mansard', ...b, 3.0, { m: 'tiles_ink', h: 1.0 });
    bands(...b, [0, 1.5, 2.8], { m: 'stone' });
    windows('z', b[3] + 0.08, b[0], b[1], { n: 3, w: 0.5, rows: [[0.45, 0.9], [1.85, 0.8]] });
    label('MANSARD + BANDS', 2, -8.2);

    b = house(6, -10, 'plain_oat', 2.4);
    roof('shed', ...b, 2.4, { m: 'tiles_sage', h: 0.9, high: '-z' });
    awning([6, 2.1, b[3]], { w: 2.4 });
    door('z', b[3], 6, { w: 1.2, m: 'glass', frame: 'card' });
    label('SHED + AWNING', 6, -8.2);

    block('tower', 9, 11, 0, 4.2, -11, -9, 'bricks_clay');
    spire([10, 4.2, -10], { h: 4.5 });
    windows('z', -9, 9, 11, { n: 2, w: 0.45, shape: 'lancet', m: 'shadow', rows: [[2.4, 1.4]] });
    label('SPIRE', 10, -8.2);

    block('drum', -11.2, -8.8, 0, 1.6, -7.2, -4.8, 'card');
    dome([-10, 1.6, -6], { r: 1.2 });
    label('DOME', -10, -4.2);

    columns([-7.4, 0, -5.4], [-4.6, 0, -5.4], { n: 4, h: 2.6, r: 0.18 });
    roof('flat', -7.6, -4.4, -6.2, -5.2, 2.6, { m: 'card', over: 0.1 });
    label('COLUMNS', -6, -4.2);

    block('porch', -3.2, -0.8, 0, 2.2, -7, -6, 'plain_stone');
    steps('+z', -6, -3.2, -0.8, { n: 3 });
    door('z', -6, -2, { y: 0.36, h: 1.7, shape: 'arch' });
    label('STEPS + DOOR', -2, -4.2);

    block('clock_wall', 1, 3, 0, 2.6, -6.6, -6, 'plain_butter_mustard');
    clock([2, 1.7, -6], { r: 0.62 });
    label('CLOCK', 2, -4.2);

    block('bell_post_a', 5.1, 5.3, 0, 2.4, -6.1, -5.9, 'wood');
    block('bell_post_b', 6.7, 6.9, 0, 2.4, -6.1, -5.9, 'wood');
    block('bell_beam', 5, 7, 2.4, 2.6, -6.15, -5.85, 'wood');
    bell([6, 2.4, -6]);
    label('BELL', 6, -4.2);

    block('shop', 8.8, 11.2, 0, 2.6, -6.8, -6, 'plain_blush');
    board([10, 2.0, -6], 'CAFÉ', { size: 0.4 });
    label('BOARD', 10, -4.2);

    // --- green things
    tree([-10.3, 0, -2], { h: 1.8, r: 0.9 });
    tree([-8.2, 0, -2], { kind: 'cone', h: 1.2, r: 0.8 });
    tree([-6.2, 0, -2], { kind: 'column', h: 1.0, r: 0.75 });
    tree([-4.2, 0, -2], { kind: 'palm', h: 2.6, r: 1.0 });
    tree([-2.2, 0, -2], { h: 1.6, r: 0.8, m: 'crown_blush' });
    label('TREES', -6.4, -0.4);
    bush([0, 0, -2]); label('BUSH', 0.2, -0.4);
    hedge([1.8, 0, -2], [4.6, 0, -2]); label('HEDGE', 3.2, -0.4);
    flowers([6.6, 0, -2], { w: 2, d: 1.2 }); label('FLOWERS', 6.6, -0.4);
    planter([9.2, 0, -2]); planter([10.6, 0, -2], { fill: 'foliage' }); label('PLANTER', 9.9, -0.4);

    // --- street furniture
    bench([-10.2, 0, 2], { rot: -90 }); person('bench', [-10.2, 0, 2], 'sit', { rot: -90, h: 0.45 }); label('BENCH', -10.2, 3.4);
    lamp([-8.3, 0, 2]); lamp([-7, 0, 2], { arm: 0.7, rot: -90 }); label('LAMP', -7.6, 3.4);
    sign([-4.8, 0, 2], 'PHỞ', { rot: -90, size: 0.42 }); label('SIGN', -4.8, 3.4);
    stall([-1.5, 0, 2], { rot: -90 }); label('STALL', -1.5, 3.9);
    cart([2.4, 0, 2], { rot: -90, words: 'CREPES' }); label('CART', 2.4, 3.4);
    seats([5.8, 0, 2], { n: 4 }).forEach((s, k) => { if (k < 2) person('seat' + k, s.at, 'sit', { rot: s.rot, h: s.h, talk: 1 }); }); label('SEATS', 5.8, 3.9);
    parasol([9.6, 0, 2]); label('PARASOL', 9.6, 3.9);

    fence([[-11, 6], [-8.6, 6], [-8.6, 7.2]], { h: 0.7, every: 0.4 }); label('FENCE', -9.8, 7.9);
    powerline([[-6.8, 6.2], [-3.4, 6.2]], { h: 3.2, sag: 0.4, tangle: 2 }); label('POWERLINE', -5.1, 7.9);
    block('post_a', -1.25, -1.15, 0, 2.6, 6.15, 6.25, 'wood'); block('post_b', 2.15, 2.25, 0, 2.6, 6.15, 6.25, 'wood');
    lanterns([-1.2, 2.6, 6.2], [2.2, 2.6, 6.2], { colors: ['red', 'butter'] }); label('LANTERNS', 0.5, 7.9);
    const bike = bicycle([4.6, 0, 6.4], { rot: 20 });
    block('basket', 0.42, 0.86, 0.72, 1.0, -0.2, 0.2, 'wood', { parent: bike });
    balls('basket_load', [[0.55, 1.08, -0.06], [0.7, 1.1, 0.06]], 0.12, 'round_red', { parent: bike });
    label('BICYCLE', 4.6, 7.9);
    fountain([8.8, 0, 6.6], { r: 1.3 }); label('FOUNTAIN', 8.8, 8.6);

    // --- things that move by themselves, and the ground
    flag([-10.6, 0, 10.4], { h: 2.4 });
    flag([-9.2, 0, 10.4], { h: 2.4, bands: ['bay', 'card', 'red'], vertical: true });
    flag([-7.8, 0, 10.4], { h: 2.4, bands: ['card'], emblem: { kind: 'disc', color: 'red' } });
    flag([-6.4, 0, 10.4], { h: 2.4, bands: ['red'], emblem: { kind: 'star', color: 'butter' } });
    label('FLAGS', -8.5, 11.5);
    const toy = group('dyn_toy', [-3.6, 0.4, 10.2], { behave: 'orbit', radius: 0.9, speed: 0.8 });
    block('toy_body', -0.3, 0.3, 0, 0.3, -0.15, 0.15, 'plain_red', { parent: toy });
    const lantern = group('dyn_lantern', [-1.2, 1.9, 10.2], { behave: 'sway', amp: 0.25 });
    sphere('lantern_ball', 0.28, [0, -0.5, 0], 'round_red', { parent: lantern, squash: [1, 1.2, 1] });
    block('lantern_post', -1.25, -1.15, 0, 1.9, 10.15, 10.25, 'wood');
    label('ORBIT  SWAY', -2.4, 11.5);
    road([[1.2, 10], [10.8, 10]], { w: 2.4 });
    zebra([6, 0, 10], { across: 2.4, deep: 1.6, rot: 0 });
    label('ROAD + ZEBRA', 6, 11.6);
  },
};
```
