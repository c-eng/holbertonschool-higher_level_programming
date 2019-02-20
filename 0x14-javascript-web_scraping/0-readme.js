#!/usr/bin/node
const fs = require('fs');
let path = process.argv[2];
if (!path) {
} else {
  fs.readFile(path, 'utf-8', function (err, fd) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(fd);
  });
}
