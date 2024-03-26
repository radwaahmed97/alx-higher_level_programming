#!/usr/bin/node

const request = require('request');
const Url = process.argv[2];

request(Url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonObject = JSON.parse(body);
    const newDictionary = {};
    let key = '';

    for (let i = 0; i < jsonObject.length; i++) {
      key = jsonObject[i].userId.toString();
      if (!newDictionary[key] && jsonObject[i].completed) {
        newDictionary[key] = 1;
      } else if (jsonObject[i].completed) {
        newDictionary[key]++;
      }
    }

    console.log(newDictionary);
  }
});
