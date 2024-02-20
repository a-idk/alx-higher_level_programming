#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const cont = JSON.parse(body);
    const chars = cont.characters;

    for (const ch of chars) {
      request.get(ch, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
