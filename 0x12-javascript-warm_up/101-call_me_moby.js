#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let idx1 = 0; idx1 < x; idx1 = idx1 + 1) {
    theFunction();
  }
};
