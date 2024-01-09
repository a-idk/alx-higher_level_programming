#!/usr/bin/node

// Returning version of a list
// @a_idk scripting

exports.esrever = function (list) {
  // declaring and assigning variables
  let length = list.length - 1;
  let idx = 0;
  let temp;

  while ((length - idx) >= 1) {
    temp = list[length];
    list[length] = list[idx];
    list[idx] = temp;
    // incrementing and decrementing the idx and length
    idx = idx + 1;
    length = length - 1;
  }
  return list;
};
