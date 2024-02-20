#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const filesys = require('fs'); // import file system module
// process.argv[0] - executable node.js, ~argv[1] - script executed
const request = require('require');
const url = process.argv[2]; // get url from command line
const filePath = process.argv[3];

request(url).pipe(filesys.createWriteStream(filePath));
