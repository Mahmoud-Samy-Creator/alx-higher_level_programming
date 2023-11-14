#!/usr/bin/node

// Script to prints x times “C is fun”

const num = parseInt(process.argv[2]);

function printing (num) {
  if (num > 0) {
    let i;

    for (i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}

printing(num);
