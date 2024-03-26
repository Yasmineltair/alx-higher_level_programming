#!/usr/bin/node

const request = require('request');
const starWars = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWars, function (_err, response, body) {
  const chars = JSON.parse(body).characters;

  for (let i = 0; i < chars.length; ++i) {
    request(chars[i], function (_cErr, _cResponse, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
