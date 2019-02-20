#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let i = 0;
    let j = 0;
    let count = 0;
    let jason = JSON.parse(body).results;
    for (i = 0; i < jason.length; i++) {
      for (j = 0; j < jason[i].characters.length; j++) {
        if (jason[i].characters[j] === 'https://swapi.co/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
