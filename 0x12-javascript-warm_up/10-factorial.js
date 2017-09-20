#!/usr/bin/node
// prints the factorial
const x = parseInt(process.argv[2]);
function fact (a) {
  if (isNaN(a) || (a === 0)) {
    return 1;
  }
  return a * fact(a - 1);
}
console.log(fact(x));
