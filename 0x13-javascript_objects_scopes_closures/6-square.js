#!/usr/bin/node

/* class Square that defines a square and inherits from Square of 5-square.js */

const mainSquare = require('./5-square');

module.exports = class Square extends mainSquare {
  charPrint (c) {
    let rows;
    if (c === undefined) {
      rows = 'X';
      for (let i = 0; i < this.width - 1; i++) {
        rows += 'X';
      }
    } else {
      rows = c;
      for (let i = 0; i < this.width - 1; i++) {
        rows += c;
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rows);
    }
  }
};
