#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const res = JSON.parse(body).results;
    for (let i = 0; i < res.length; i++) {
      if (res[i]['characters'].includes('https://swapi.co/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
