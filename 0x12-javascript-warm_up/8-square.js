#!/usr/bin/node
let i = 0;
let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
