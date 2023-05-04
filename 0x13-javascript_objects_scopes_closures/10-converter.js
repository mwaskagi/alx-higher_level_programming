#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
