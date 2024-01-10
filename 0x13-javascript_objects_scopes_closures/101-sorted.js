#!/usr/bin/node

// script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence
// @a_idk scripting

const dict = require('./101-data.js').dict;
const objDict = {};

for (const x in dict) {
  if (objDict[dict[x]] === undefined) {
    objDict[dict[x]] = [x];
  } else {
    objDict[dict[x]].push(x);
  }
}

console.log(objDict);
