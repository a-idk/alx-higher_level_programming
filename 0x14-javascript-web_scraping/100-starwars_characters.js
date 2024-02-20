#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    chars.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
