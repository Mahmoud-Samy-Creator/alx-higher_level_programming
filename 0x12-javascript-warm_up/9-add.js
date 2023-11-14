#!/usr/bin/node

// Script to add two integers

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(process.argv[2], process.argv[3]);
