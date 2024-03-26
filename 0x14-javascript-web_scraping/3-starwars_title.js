#!/usr/bin/node

const request = require('request');
const starWars = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWars, function (_err, response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
