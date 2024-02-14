#!/usr/bin/node
const file = require('fs');

const firstfile = file.readFileSync(process.argv[2]).toString();
const secondfile = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], firstfile + secondfile);
