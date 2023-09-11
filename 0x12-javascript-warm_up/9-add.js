#!/usr/bin/node

if (isNaN(process.argv[2] || isNaN(process.argv[3]))) {
  console.log(NaN);
} else {
  function add (a, b) {
    return (a + b);
  }
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
}
