#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  let x = 0;

  while (list[x]) {
    if (searchElement === list[x]) {
      occ += 1;
    }
    x += 1;
  }
  return occ;
};
