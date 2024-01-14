#!/usr/bin/node

// Returning occurrencies in a list

exports.nbOccurences = function (list, searchElement) {
  let numOccurr = 0;

  for (let idx1 = 0; idx1 < list.length; idx1 += 1) {
    if (searchElement === list[idx1]) {
      numOccurr = numOccurr + 1;
    }
  }
  return numOccurr;
};
