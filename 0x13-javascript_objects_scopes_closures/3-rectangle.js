#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// You must use the class notation for defining your class
// The constructor must take 2 arguments width and height
// If w or h is equal to 0 or not a positive integer, create an empty object
module.exports = class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0 && width !== undefined && height !== undefined) {
      this.width = width;
      this.height = height;
    }
  }

  // method
  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }
};
