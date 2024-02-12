#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let k = 0; k < process.argv[2]; k++) {
    let row = '';
    for (let j = 0; j < process.argv[2]; j++) row += 'X';
    console.log(row);
  }
}
