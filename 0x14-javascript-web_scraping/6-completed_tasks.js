#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let dict = {};
if (!url) {
} else {
  request.get(url, 'utf-8', function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let jason = JSON.parse(body);
      let i = 0;
      for (i = 0; i < jason.length; i++) {
        if (jason[i].completed) {
          if (jason[i].userId in dict) {
            dict[jason[i].userId] += 1;
          } else {
            dict[jason[i].userId] = 1;
          }
        }
      }
      console.log(dict);
    }
  });
}
