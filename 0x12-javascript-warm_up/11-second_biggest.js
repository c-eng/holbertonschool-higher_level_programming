#!/usr/bin/node
let first = 0;
let second = 0;
let i = 2;
let len = process.argv.length;
if (len < 4) {
  console.log('0');
} else {
  for (; i < len; i++) {
    if (process.argv[i] >= first) {
      second = first;
      first = process.argv[i];
    } else if (process.argv[i] >= second) {
      second = process.argv[i];
    }
  }
  console.log(second);
}
