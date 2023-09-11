#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let x = 0;

  while (x < parseInt(process.argv[2]) && parseInt(process.argv[2]) > 0) {
    let y = 0;
    const arr = [];
    while (y < parseInt(process.argv[2])) {
      arr.push('X');
      y += 1;
    }
    console.log(...arr);
    x += 1;
  }
}
