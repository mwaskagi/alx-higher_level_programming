#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const x in list) {
    if (list[x] === searchElement) {
      count++;
    }
  }
  return (count);
};
