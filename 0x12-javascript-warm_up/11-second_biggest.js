#!/usr/bin/node
let first = Number.MIN_SAFE_INTEGER;
let second = Number.MIN_SAFE_INTEGER;
let i = 2;
let len = process.argv.length;
if (len < 4) {
  console.log('0');
} else {
  for (; i < len; i++) {
    if (parseInt(process.argv[i]) > first) {
      second = first;
      first = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > second) {
      second = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
