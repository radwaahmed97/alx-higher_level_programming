#!/usr/bin/node
const SquareParent = require('./5-square');
module.exports = class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 1; i <= this.height; i++) {
      let sp = '';
      for (let j = 1; j <= this.width; j++) {
        sp += c;
      }
      console.log(sp);
    }
  }
};
