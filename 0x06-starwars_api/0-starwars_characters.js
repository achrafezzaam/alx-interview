#!/usr/bin/node

const request = require('request');

const order = (actors, x) => {
  if (x !== actors.length) {
    request(actors[x], function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
      order(actors, x + 1);
    });
  }
};

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  order(actors, 0);
});
