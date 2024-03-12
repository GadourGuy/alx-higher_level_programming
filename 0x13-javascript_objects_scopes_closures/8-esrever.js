#!/usr/bin/node
exports.esrever = function (list) {
  let tmp;
  for (let i = 0; i < Math.floor(list.length / 2); i++) {
    tmp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = tmp;
  }
  return (list);
};
