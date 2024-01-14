#!/usr/bin/node

// Rectangle Class that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
