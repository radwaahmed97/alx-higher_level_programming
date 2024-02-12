#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log(1);
} else {
  function factorial (num) {
    if (num < 0) {
      return (-1);
    }
    if (num === 0) {
      return (1);
    } else {
      return (num * factorial(num - 1));
    }
  }
  console.log(factorial(Number(process.argv[2])));
}
