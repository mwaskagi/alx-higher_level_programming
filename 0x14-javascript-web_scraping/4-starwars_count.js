#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const args = process.argv;
let reqURL = args[2];
let request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const x in results) {
      const chars = results[x].characters;
      for (const y in chars) {
        if (chars[y].search('/18/') > 0) {
          count++;
        }
      }
    }
   console.log(count);
  }
});
