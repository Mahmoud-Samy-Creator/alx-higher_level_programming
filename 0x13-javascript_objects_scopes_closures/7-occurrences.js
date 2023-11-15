#!/usr/bin/node

/* function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let num = 0;

  for (const number of list) {
    if (number === searchElement) {
      num += 1;
    }
  }
  return (num);
};
