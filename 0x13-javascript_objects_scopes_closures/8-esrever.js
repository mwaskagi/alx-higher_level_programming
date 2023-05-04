#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.esrever = function (list) {
  const reverse = [];
  for (const x in list) {
    reverse.unshift(list[x]);
  }
  return (reverse);
};
