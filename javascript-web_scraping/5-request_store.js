#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const fs = require('fs');

request(argv[2], argv[3], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(argv[3], body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
