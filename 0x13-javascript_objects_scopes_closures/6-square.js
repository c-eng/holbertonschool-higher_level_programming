#!/usr/bin/node
const Square0 = require('./5-square');
module.exports = class Square extends Square0 {
  charPrint (c) {
    if (c) {
      let i = 0;
      for (; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
