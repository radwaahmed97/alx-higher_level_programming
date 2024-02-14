#!/usr/bin/node
const dict = require('./101-data').dict;
const list = Object.entries(dict);
const values = Object.values(dict);
const uniqevalues = [...new Set(values)];
const newdict = {};
for (const j in uniqevalues) {
  const pot = [];
  for (const k in list) {
    if (list[k][1] === uniqevalues[j]) {
      pot.unshift(list[k][0]);
    }
  }
  newdict[uniqevalues[j]] = pot;
}
console.log(newdict);
