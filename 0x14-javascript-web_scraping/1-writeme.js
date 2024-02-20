#!/usr/bin/node

const filesys = require('fs'); // import file system module
// process.argv[0] - executable node.js, ~argv[1] - script executed
const filePath = process.argv[2]; // get file name from command line
const content = process.argv[3];

filesys.writeFile(filePath, content, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
