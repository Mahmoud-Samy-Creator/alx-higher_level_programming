#!/usr/bin/node
/**
 * Reads and prints contents of a file */


/* Step [1]
Creating fs [file system ] object to interact with a file
using file system module bult-in in javascript
*/
const fs = require('fs');

/**
* Use readFile method to write to a file
 */
fs.readFile(process.argv[2], 'utf8', function (err, data) {
	if (err) console.log(err);
	else process.stdout.write(data);
});
