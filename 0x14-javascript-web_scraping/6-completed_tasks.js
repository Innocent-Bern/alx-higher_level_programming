#!/usr/bin/node

const request = require('request');

const url = `${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const completed = {};
    JSON.parse(body).forEach((element) => {
      if (completed[`${element.userId}`] === undefined) {
        completed[`${element.userId}`] = 0;
      }
      if (element.completed) {
        completed[`${element.userId}`] += 1;
      }
    });
    console.log(completed);
  }
});
