#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(Rectangle);
    this.height = size;
    this.width = size;
  }
}

module.exports = Square;
