#!/usr/bin/node
// prints number of movies where character “Wedge Antilles” is present
const request = require('request');
// process.argv[0] - executable node.js, ~argv[1] - script executed
const movieId = process.argv[2];

// const link = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(movieId, function (error, response, body) {
  if (!error) {
    const output = JSON.parse(body).results;
    console.log(output.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
