#!/usr/bin/node

// Square Class that inherits from Rectangle Class
// @a_idk scripting

const Square6 = require('./5-square');

class Square extends Square6 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let idx1 = 0; idx1 < this.height; idx1 += 1) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
