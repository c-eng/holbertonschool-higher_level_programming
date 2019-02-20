#!/usr/bin/node
const fs = require('fs');
let path = process.argv[2];
let text = process.argv[3];
if (!path || !text) {
} else {
  text += '\n';
  fs.writeFile(path, text, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
}
