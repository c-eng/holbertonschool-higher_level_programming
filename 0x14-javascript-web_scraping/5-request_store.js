#!/usr/bin/node
const request = require('request');
const fs = require('fs');
let url = process.argv[2];
let path = process.argv[3];
if (!url || !path) {
} else {
  request.get(url, 'utf-8', function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(path, body, 'utf-8', function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
