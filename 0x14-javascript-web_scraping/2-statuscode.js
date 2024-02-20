#!/usr/bin/node

const req = require('request');
// process.argv[0] - executable node.js, ~argv[1] - script executed
const url = process.argv[2]; // get URL from command line

req(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode); // print format given
  }
});
