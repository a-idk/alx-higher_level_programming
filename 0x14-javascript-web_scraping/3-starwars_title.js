#!/usr/bin/node
// prints title of a Star Wars movie with episode no. matches an int
const request = require('request');
// process.argv[0] - executable node.js, ~argv[1] - script executed
const movieId = process.argv[2];

const link = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(link, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
