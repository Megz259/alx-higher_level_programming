#!/usr/bin/node
const dict = require('./101-data').dict;
let newDict = {};
let key;
for (key in dict) {
	newDict[dict[key]] = [];
}
for (key in dict) {
	newDict[dict[key]].push(key);
}
function cmp (a, b) {
	return a - b;
}
for (k in newDict) {
	newDict[key].sort(cmp);
}
console.log(newDict);
