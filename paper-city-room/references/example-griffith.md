# A finished room: Griffith Observatory

images/good-griffith-whole.jpg is how it draws. One landmark built from blocks, a drum and domes; a lawn with a monument; a drive with cars; 15 people.

```js
// Griffith Observatory, Los Angeles: the white Art Deco observatory with its three copper domes on the brow of
// Mount Hollywood, the Astronomers Monument on the lawn in front, a drive round the lawn, and the HOLLYWOOD
// sign on the hill behind.
import { block, box, cyl, lathe, terrain, text, flatsY, rect, person, dog, traffic, oval } from '../../src/kit.js';
import { tree, bench, lamp, flag, windows, door, bands, steps, dome, road, bush, sign } from '../../src/parts.js';

// the building: a long white front along x at the back, the rotunda in the middle, a wing at each end
const FZ = -6;                       // the front wall (faces +z)
const DRIVE = oval(1, 2.5, 8, 6.2, { n: 40, exp: 0.55 });   // the drive round the lawn
const hill = (x, z) => Math.max(0, -9.6 - x) * 0.75;

export default {
  icon: 'M3 20h18M5 20v-6h14v6M8 14a4 4 0 0 1 8 0M12 8V6',
  slab: 'paving',
  model() {
    // Mount Lee behind, with the sign on its brow
    terrain('mtlee', 10, 24, -12, -9.4, -12, 12, hill, 'hill');
    text('hollywood', 'HOLLYWOOD', [-10.5, 1.75, 0.5], { h: 1.8, face: 0, m: 'chalk' });

    // the main hall and the rotunda
    block('hall', -6, 6, 0, 4.2, -10, FZ, 'card');
    bands(-6, 6, -10, FZ, [0, 3.9], { m: 'stone' });
    windows('z', FZ, -5.5, -2.6, { n: 3, y: 1.4, h: 1.8, w: 0.45, frame: 'stone' });
    windows('z', FZ, 2.6, 5.5, { n: 3, y: 1.4, h: 1.8, w: 0.45, frame: 'stone' });
    windows('x', 6, -9.5, -6.5, { n: 3, y: 1.4, h: 1.8, w: 0.45, frame: 'stone' });
    block('portal', -2.2, 2.2, 0, 5.4, -7, -5.6, 'card');
    windows('z', -5.6, -1.8, 1.8, { n: 3, y: 2.6, h: 2.2, w: 0.55, shape: 'arch', frame: 'stone' });
    door('z', -5.6, 0, { w: 1.6, h: 2.2, m: 'plain_graphite' });
    steps('+z', -5.6, -2.4, 2.4, { n: 3 });
    cyl('drum', 3, 1.3, [0, 4.2, -8.2], 'card', { segs: 24 });
    dome([0, 5.5, -8.2], { r: 3, h: 3.1, m: 'plain_sage_moss', segs: 24, lantern: 0 });
    cyl('finial', 0.25, 0.7, [0, 8.55, -8.2], 'card', { segs: 8 });

    // the two wings, each with its telescope dome
    for (const s of [-1, 1]) {
      const x0 = s < 0 ? -9.4 : 6, x1 = s < 0 ? -6 : 9.4, cx = s * 7.7;
      block(`wing${s}`, x0, x1, 0, 3.8, -10.2, -6.4, 'card');
      bands(x0, x1, -10.2, -6.4, [3.5], { m: 'stone' });
      windows('z', -6.4, cx - 1, cx + 1, { n: 2, y: 1.3, h: 1.6, w: 0.4, frame: 'stone' });
      cyl(`wingdrum${s}`, 1.5, 0.6, [cx, 3.8, -8.3], 'card', { segs: 18 });
      dome([cx, 4.4, -8.3], { r: 1.5, m: 'plain_sage_moss', lantern: 0, name: `wingdome${s}` });
    }
    windows('x', 9.4, -9.6, -7, { n: 2, y: 1.3, h: 1.6, w: 0.4, frame: 'stone' });

    // the terrace and the lawn with the Astronomers Monument
    flatsY('lawn', 0.01, [rect(-3.8, 5.8, -1.4, 6.4)], 'lawn');
    box('monument_base', [1.6, 0.6, 1.6], [1, 0, 2.5], 'stone');
    box('monument', [0.8, 4.2, 0.8], [1, 0.6, 2.5], 'card', { taper: [0.55, 0.55] });
    lathe('monument_star', [[0, 0], [0.35, 0.2], [0, 0.5]], [1, 4.8, 2.5], 'plain_mustard', { segs: 6 });
    for (const [x, z] of [[-3, -1], [5, -1], [-3, 6], [5, 6]]) bush([x, 0, z], { r: 0.5 });

    // the drive, palms and lamps outside it
    road(DRIVE, { closed: true, w: 2 });
    traffic(DRIVE, { vehicles: ['car_sky', 'car_mustard', 'car_fig'], speed: 2.2, size: 0.9 });
    for (const [x, z, h] of [[10.8, -4, 6], [10.8, -9, 5.5], [-9.2, -3.5, 5], [-9, 10, 4]]) tree([x, 0, z], { kind: 'palm', h, r: 1.4 });
    for (const [x, z] of [[-8.6, 1.5], [10.6, 6], [-3, 10.6]]) lamp([x, 0, z]);
    flag([-4.5, 0, -5], { bands: ['red', 'card', 'bay'] });
    sign([10.6, 0, 9.4], 'GRIFFITH OBSERVATORY', { rot: -45, size: 0.3 });

    // the terrace railing: people looking out over the basin, and a coin telescope
    cyl('scope_post', 0.06, 1, [-7.5, 0, -4.8], 'plain_graphite', { segs: 6 });
    box('scope', [0.5, 0.25, 0.25], [-7.5, 1, -4.8], 'plain_mustard');
    person('looker', [-7.5, 0, -4.2], 'photo', { rot: 90 });
    person('pointer', [-6.6, 0, -4.4], 'point', { rot: 60 });
    person('friend', [-5.9, 0, -4.6], 'stand', { rot: 70 });
    person('guide', [0, 0, -4.6], 'wave', { rot: -90, top: 'sky' });
    person('visitor1', [-1.5, 0, -4.4], 'talk', { rot: 0 });
    person('visitor2', [-0.7, 0, -4.3], 'talk', { rot: 180 });
    person('selfie', [2.4, 0, 0.3], 'photo', { rot: 120 });
    person('picnic1', [-2.2, 0, 4.6], 'sit_ground', { rot: -30 });
    person('picnic2', [-1.4, 0, 5.1], 'sit_ground', { rot: 150 });
    person('sunbather', [4, 0, 4.6], 'lie', { rot: 30 });
    person('reader', [-8.6, 0, 4.5], 'sit', { rot: 0, h: 0.45 });
    bench([-8.6, 0, 4.5], { rot: 0 });
    person('hiker', [-8.8, 0, -1], 'walk', { to: [-8.8, 0, 9], hat: 'mustard' });
    person('jogger', [11.2, 0, -2], 'jog', { to: [11.2, 0, 10], top: 'red' });
    person('stroller', [-4, 0, 11.2], 'walk', { to: [8, 0, 11.2] });
    person('kid', [3.6, 0, 1.4], 'cheer', { rot: -45 });
    dog('comet', [0.4, 0, 0.6], 'run_circle', { radius: 1.2 });
  },
};
```
