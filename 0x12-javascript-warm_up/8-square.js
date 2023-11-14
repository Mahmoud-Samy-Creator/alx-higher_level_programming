#!/usr/bin/node

// Script to print square of size argv[2].

const arg = parseInt(process.argv[2]);

function squarePrint (arg) {
  if (!arg) {
    console.log('Missing size');
  } else {
    let row = 'X';
    let i;
    let j;

    for (i = 0; i < arg; i++) {
      for (j = 0; j < arg - 1; j++) {
        row = row + 'X';
      }
      console.log(row);
      row = 'X';
    }
  }
}

squarePrint(arg);
