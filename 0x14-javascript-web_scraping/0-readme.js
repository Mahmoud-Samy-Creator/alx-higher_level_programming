#!/usr/bin/node

/* Reads & prints file contents */

/* Step [1]
Creating fs [file system ] object to interact with a file
using file system module bult-in in javascript
*/

const fs = require('fs');

/* Step [2]
If an error occurred during the reading, print the error object
 */
fs.readFile(process.argv[2], function (err, data) {
    if (err) console.log(err);
    else process.stdout.write(data);
});
