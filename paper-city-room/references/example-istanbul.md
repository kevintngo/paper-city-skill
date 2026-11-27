# A finished room: Ayasofya, Istanbul

Written by an agent from this skill, then corrected: `stall` takes lists of colors (`awning: ['red', 'card']`), a
`traffic` route takes `[x, y, z]` points, and the jogger was moved off the tram line. A mosque of blocks, domes and four
minarets at the back; a tram across the middle; a square with a fountain, tulips, tea and a simit cart in front.

```js
// Istanbul, Sultanahmet: Hagia Sophia (Ayasofya) at the back, its pink walls under a lead-gray dome with half
// domes either side and four pencil minarets, a square with a fountain and tulips, the T1 tram along the
// street in front, and a near strip of simit carts, tea glasses, a bazaar stall and lanterns.
import { block, cyl, flatsY, rect, person, cat, traffic } from '../../src/kit.js';
import { tree, bench, lamp, flag, windows, door, bands, dome, road, flowers, fountain, sign, stall, cart, seats, lanterns } from '../../src/parts.js';

// the mosque: low aisles all round, a taller central block, the great dome over the middle
const AX0 = -8, AX1 = 2, AZ0 = -11, AZ1 = -4;      // aisles footprint
const CX0 = -6.5, CX1 = 0.5, CZ0 = -10.5, CZ1 = -4.5; // central block
const DC = [-3, -7.5];                              // dome center [x, z]
const MINARETS = [[-9.6, -11.4], [3.4, -11.4], [-9.6, -3.2], [3.4, -3.2]];
const TRAM = [[-11, 0, 5], [11, 0, 5]];             // the tram line, z 3.5..6.5: points [x, y, z]

export default {
  icon: 'M3 20h18M7 20v-7a5 5 0 0 1 10 0v7M4 20V7M20 20V7',
  slab: 'paving',
  model() {
    // Hagia Sophia
    block('aisles', AX0, AX1, 0, 4, AZ0, AZ1, 'blush');
    bands(AX0, AX1, AZ0, AZ1, [3.7], { m: 'card' });
    windows('z', AZ1, -7.5, -4.2, { n: 3, y: 1.1, h: 1.8, w: 0.5, shape: 'arch', frame: 'card' });
    windows('z', AZ1, -1.8, 1.5, { n: 3, y: 1.1, h: 1.8, w: 0.5, shape: 'arch', frame: 'card' });
    door('z', AZ1, -3, { w: 1.8, h: 2.6, m: 'plain_graphite' });
    windows('x', AX1, -10.5, -4.5, { n: 4, y: 1.1, h: 1.8, w: 0.5, shape: 'arch', frame: 'card' });

    block('nave', CX0, CX1, 4, 6, CZ0, CZ1, 'blush');
    bands(CX0, CX1, CZ0, CZ1, [5.8], { m: 'card' });
    windows('z', CZ1, -5.8, -0.2, { n: 6, y: 4.4, h: 1.1, w: 0.45, shape: 'arch', frame: 'card' });
    windows('x', CX1, -10, -5, { n: 4, y: 4.4, h: 1.1, w: 0.45, shape: 'arch', frame: 'card' });

    // half domes east and west, then the drum and the great dome
    dome([DC[0] - 3.2, 6, DC[1]], { r: 2.4, h: 2.0, m: 'plain_mist_graphite', lantern: 0, name: 'halfdome_w' });
    dome([DC[0] + 3.2, 6, DC[1]], { r: 2.4, h: 2.0, m: 'plain_mist_graphite', lantern: 0, name: 'halfdome_e' });
    cyl('drum', 3.4, 1.2, [DC[0], 6, DC[1]], 'blush', { segs: 24 });
    dome([DC[0], 7.2, DC[1]], { r: 3.4, h: 2.7, m: 'plain_mist_graphite', segs: 24, lantern: 0, name: 'greatdome' });
    cyl('finial', 0.08, 1.0, [DC[0], 9.9, DC[1]], 'plain_mustard', { segs: 6 });

    // four minarets: shaft, balcony, pencil cap
    MINARETS.forEach(([x, z], i) => {
      cyl(`min_base${i}`, 0.6, 2, [x, 0, z], 'card', { segs: 8, smooth: false });
      cyl(`min_shaft${i}`, 0.35, 11, [x, 2, z], 'card', { segs: 12 });
      cyl(`min_balcony${i}`, 0.6, 0.25, [x, 9.5, z], 'card', { segs: 12 });
      cyl(`min_cap${i}`, 0.4, 2.6, [x, 13, z], 'plain_mist_graphite', { segs: 12, r2: 0 });
    });

    // the square: tulips and cypresses on the lawn, the fountain, a flag
    flatsY('lawn', 0.01, [rect(4.5, 11.5, -11.5, -5.5)], 'lawn');
    flowers([8, 0, -8.5], { w: 5, d: 3, colors: ['red', 'mustard', 'blush'] });
    for (const [x, z] of [[11, -11], [11, -6.5], [5, -11]]) tree([x, 0, z], { kind: 'column', h: 4.5, r: 0.7 });
    tree([-11, 0, 1.5], { kind: 'round', h: 2.5, r: 1.4 });
    fountain([6.5, 0, -1.5], { r: 1.4, jets: 5 });
    flag([10.8, 0, -3], { bands: ['red'], emblem: { kind: 'star', color: 'card', r: 0.35 } });
    bench([-6, 0, 1], { rot: 0 });
    for (const [x, z] of [[-10.5, 2.6], [1, 2.6], [10.8, 2.6]]) lamp([x, 0, z]);

    // the T1 tram along the street
    road(TRAM, { w: 3, dash: null });
    traffic(TRAM, { vehicles: ['tram'], speed: 2 });

    // the near strip, kept low: a bazaar stall under lanterns, tea, the simit cart, the sign
    stall([-7, 0, 9.5], { awning: ['red', 'card'], goods: ['mustard', 'red'] });
    lanterns([-10.5, 2.6, 8], [-3.5, 2.6, 8], {});
    const tea = seats([1, 0, 9.5], { n: 4 });
    cart([7, 0, 9], { words: 'SİMİT', rot: -45 });
    sign([10.6, 0, 10.6], 'AYASOFYA', { rot: -45, size: 0.3 });

    // people
    tea.forEach((s, i) => person(`tea${i}`, s.at, 'sit', { rot: s.rot, h: s.h }));
    person('simitci', [7.8, 0, 9.8], 'wave', { rot: 135, hat: 'red' });
    person('seller', [-7, 0, 10.6], 'talk', { rot: 90 });
    person('shopper', [-5.6, 0, 10.8], 'talk', { rot: -90, top: 'sky' });
    person('reader', [-6, 0, 1], 'sit', { rot: 0, h: 0.45 });
    person('tourist1', [-3, 0, -1], 'photo', { rot: 90, hat: 'mustard' });
    person('tourist2', [-2, 0, -0.6], 'point', { rot: 100 });
    person('guide', [-4.2, 0, -2.2], 'wave', { rot: -60, top: 'jade' });
    person('kid', [5, 0, 0], 'cheer', { rot: 30 });
    person('walker1', [-10, 0, 2], 'walk', { to: [9, 0, 2] });
    person('walker2', [-11, 0, 11.4], 'walk', { to: [5, 0, 11.4], top: 'fig' });
    person('jogger', [-10, 0, 7.4], 'jog', { to: [10, 0, 7.4], top: 'red' });
    cat('tekir', [-1.2, 0, -2.6], 'sit');
    cat('pamuk', [4.5, 0, 8.2], 'sit');
  },
};
```
