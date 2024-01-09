#!/usr/bin/node

const arg = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  return a + b;
}

console.log(add(Number(arg), Number(arg2)));
