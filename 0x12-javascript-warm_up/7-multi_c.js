#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let x = 0;
  while (x < parseInt(process.argv[2])) {
    console.log('C is fun');
    x += 1;
  }
}
