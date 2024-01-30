#!/usr/bin/node
/* A script that display the status code of a git request */


/**
 * Make request object using built-in request
 */
const request = require('request')


/**
 * Using get, on method to log the status code
 */
request.get(process.argv[2]).on('response', function (response) {
	console.log('code:', response.statusCode);
});
