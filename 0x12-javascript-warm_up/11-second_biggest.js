#!/usr/bin/node
const size = process.argv.length;
if ((process.argv[2] === undefined) || (size === 3)) {
  console.log(0);
} else {
  const desc = [];
  for (let i = 2; i < size; i++) {
    desc[i - 2] = parseInt(process.argv[i]);
  }
  desc.sort(function (a, b) { return b - a; });
  console.log(desc[1]);
}
