#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.logMe = (function (item) {
  let id = 0;
  return function (item) { return console.log('%d: %s', id++, item); };
}
)();
