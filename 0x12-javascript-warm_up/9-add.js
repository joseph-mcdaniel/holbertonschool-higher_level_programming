#!/usr/bin/node
// prints the addition of 2 ints
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}
console.log(add(x, y));
