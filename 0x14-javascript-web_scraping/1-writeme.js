#!/usr/bin/node
/**
 * Writes string to file
 * First arg is file path
 * Second arg is string
 */


/* Step [1]
Creating fs [file system ] object to interact with a file
using file system module bult-in in javascript
*/
const fs = require('fs');

/*
Use writeFile method to write to a file
 */
fs.writeFile(process.argv[2], process.argv[3], (err) => {
	if (err) console.log(err);
});

