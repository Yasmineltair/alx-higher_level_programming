#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_err, rec) {
  console.log('code:', rec.statusCode);
});
