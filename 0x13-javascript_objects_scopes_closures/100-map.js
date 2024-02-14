#!/usr/bin/node
const list = require('./100-data').list;
/*
const newlist = [];
for (let i = 0; i < list.length; i++) {
  newlist.push(list[i] * i);
}
console.log(newlist);
*/
console.log(list.map((element, i) => element * i));
