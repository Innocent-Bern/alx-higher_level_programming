#!/usr/bin/node

async function statusCode () {
  const response = await fetch(`${process.argv[2]}`);
  console.log(`code: ${response.status}`);
}
statusCode();
