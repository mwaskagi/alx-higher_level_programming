#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// You must use the class notation for defining your class
// The constructor must take 2 arguments width and height
// If w or h is equal to 0 or not a positive integer, create an empty object
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0 && width !== undefined && height !== undefined) {
      this.width = width;
      this.height = height;
    }
  }

  // method print
  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  // method rotate
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Rectangle;
module.exports = Square;
