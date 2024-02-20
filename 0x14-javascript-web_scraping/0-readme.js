#!/usr/bin/node

const filesys = require('fs'); // import file system module
// process.argv[0] - executable node.js, ~argv[1] - script executed
const filePath = process.argv[2]; // get file name from command line

filesys.readFile(filePath, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
