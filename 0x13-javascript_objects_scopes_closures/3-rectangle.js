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
      let arr = '';

      while (y < this.width) {
        arr += 'X';
        y += 1;
      }
      console.log(arr);
      x += 1;
    }
  }
}

module.exports = Rectangle;
