#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  if (list && searchElement) {
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) { occurences += 1; }
    }
  }
  return (occurences);
};
