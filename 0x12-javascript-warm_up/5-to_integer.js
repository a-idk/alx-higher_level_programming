#!/usr/bin/node

// declaring and initializing variables
const arg = process.argv;
const n = parseInt(arg);

if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${n}`);
}
