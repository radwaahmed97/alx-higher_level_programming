#!/usr/bin/node

const request = require('request');
const Url = process.argv[2];
const storedfile = process.argv[3];

request(Url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');

    fs.writeFile(storedfile, body, 'utf-8', (err) => {
      if (err) {
        return console.error(err);
      }
    });
  }
});
