#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    JSON.parse(body).characters.forEach(element => {
      request(element, (err, res, bdy) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(bdy).name);
        }
      });
    });
  }
});
