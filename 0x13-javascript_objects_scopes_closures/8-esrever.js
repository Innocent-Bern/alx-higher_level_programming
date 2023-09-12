#!/usr/bin/node

exports.esrever = function (list) {
  const cpy = [...list];
  let x = 0;

  while (x < cpy.length) {
    list[cpy.length - 1 - x] = cpy[x];
    x += 1;
  }
  return list;
};
