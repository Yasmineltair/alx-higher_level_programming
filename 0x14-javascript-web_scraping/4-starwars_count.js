#!/usr/bin/node

const request = require('request');
const starWars = process.argv[2];
let times = 0;

request(starWars, function (_err, response, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const chars = body[i].characters;

    for (let j = 0; j < chars.length; ++j) {
      const character = chars[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }
  console.log(times);
});
