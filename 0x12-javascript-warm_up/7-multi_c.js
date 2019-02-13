#!/usr/bin/node
let i = 0;
let num = parseInt(process.argv[2]);
if (isNaN(num)){
  console.log('Missing number of occurrences');
} else {
  for (; i < num; i++) {
    console.log('C is fun');
  }
}
