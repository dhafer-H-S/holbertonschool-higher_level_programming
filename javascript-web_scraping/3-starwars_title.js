#!/usr/bin/node

const request = require('request');
const apiurl = 'https://swapi-api.hbtn.io/api/films/';
const argv = process.argv;

request.get(apiurl + argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
