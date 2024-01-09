#!/usr/bin/node

const arg = process.argv[2];
const idx1 = Number(arg);

if (arg === undefined || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  // const idx1 = Number(arg);
  let idx2 = 0;
  while (idx2 < idx1) {
    console.log('C is fun');
    idx2 = idx2 + 1;
  }
}
