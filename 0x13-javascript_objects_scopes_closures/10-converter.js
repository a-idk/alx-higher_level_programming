#!/usr/bin/node

// converts a number from base 10 to another base passed as argument
// @a_idk scripting

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
