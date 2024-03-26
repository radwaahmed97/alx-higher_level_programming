#!/usr/bin/node

const request = require('request');
const StarWarsUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(StarWarsUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characterUrl = JSON.parse(body).characters;

  for (let i = 0; i < characterUrl.length; i++) {
    request(characterUrl[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
