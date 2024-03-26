#!/usr/bin/node

const request = require('request');
const StarWarsUrl = process.argv[2];

request(StarWarsUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (body) {
    const json = JSON.parse(body);
    const charFilms = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
