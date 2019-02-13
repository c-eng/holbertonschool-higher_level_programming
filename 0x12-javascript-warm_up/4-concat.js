#!/usr/bin/node
let first = 'undefined';
let second = 'undefined';
if (process.argv[2]) {
  first = process.argv[2];
}
if (process.argv[3]) {
  second = process.argv[3];
}
console.log(first + ' is ' + second);
