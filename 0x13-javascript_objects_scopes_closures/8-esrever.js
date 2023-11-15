#!/usr/bin/node

/* A function that returns the reversed version of a list */

exports.esrever = function (list) {
  let start = 0;
  let end = list.length - 1;
  let temp;

  while (start < end) {
    temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    start++;
    end--;

    return list;
  }
};
