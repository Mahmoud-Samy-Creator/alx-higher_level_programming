#!usr/bin/node

/* A class defines a rectangle */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let row = '';
      let i;
      for (i = 0; i < this.width; i++) {
        row = row + 'X';
      }
      for (i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
