#!/usr/bin/node

const arg = process.argv[2];
const idx1 = Number(arg);

if (arg === undefined || isNaN(arg)) {
  console.log('Missing size');
} else {
  let idx2 = 0;
  while (idx2 < idx1) {
    console.log('X'.repeat(idx1));
    idx2 = idx2 + 1;
  }
}
