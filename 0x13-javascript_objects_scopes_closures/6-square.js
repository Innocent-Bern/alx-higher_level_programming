#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(Rectangle);
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      let x = 0;

      while (x < this.height) {
        let y = 0;
        const arr = [];

        while (y < this.height) {
          arr.push('C');
          y += 1;
        }
        console.log(...arr);
        x += 1;
      }
    }
  }
}

module.exports = Square;
