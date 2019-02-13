#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
let first = parseInt(process.argv[2]);
let second = parseInt(process.argv[3]);
console.log(add(first, second));
