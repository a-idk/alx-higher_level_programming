#!/usr/bin/node

// if no argument
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2).map(Number);
  const args = array.sort(function (first, second) { return second - first; })[1];

  console.log(args);
}
