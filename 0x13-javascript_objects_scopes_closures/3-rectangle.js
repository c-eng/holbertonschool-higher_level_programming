#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    let width = parseInt(w);
    let height = parseInt(h);
    if (isNaN(width) || isNaN(height) || width < 1 || height < 1) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
