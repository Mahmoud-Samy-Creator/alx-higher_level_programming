#!/usr/bin/node

// Script to print ints passed as arguments to the script.

const arg = parseInt(process.argv[2]);
if (!arg) {
  console.log('Not a number');
} else {
  console.log(arg);
}
