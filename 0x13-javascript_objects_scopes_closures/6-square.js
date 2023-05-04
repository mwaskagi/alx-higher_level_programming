#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// You must use the class notation for defining your class
// The constructor must take 2 arguments width and height
// If w or h is equal to 0 or not a positive integer, create an empty object
const SquareR = require('./5-square');

class Square extends SquareR {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
