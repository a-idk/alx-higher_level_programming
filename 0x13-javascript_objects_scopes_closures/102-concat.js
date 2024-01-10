#!/usr/bin/node

// Script that concats 2 files
// @a_idk scripting

const arg = process.argv;
const filePath = require('fs');
const source1 = filePath.readFileSync(arg[2], 'utf8');
const source2 = filePath.readFileSync(arg[3], 'utf8');
filePath.writeFileSync(arg[4], source1 + source2);
