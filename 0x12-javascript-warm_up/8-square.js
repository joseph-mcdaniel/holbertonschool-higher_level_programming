#!/usr/bin/node
// print square
const num = process.argv[2];
if (isNaN(num) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let square = '';
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
