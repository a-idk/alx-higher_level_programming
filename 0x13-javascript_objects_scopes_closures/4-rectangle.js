#!/usr/bin/node

// Rectangle Class that defines a rectangle with character X
// rotate and double inclusive
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const xter = 'X';
    for (let idx1 = 0; idx1 < this.height; idx1 += 1) {
      console.log(xter.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
