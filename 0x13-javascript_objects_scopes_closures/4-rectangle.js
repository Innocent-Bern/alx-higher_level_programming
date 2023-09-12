#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;

    while (x < this.height) {
      let y = 0;
      const arr = [];

      while (y < this.width) {
        arr.push('X');
        y += 1;
      }
      console.log(...arr);
      x += 1;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
