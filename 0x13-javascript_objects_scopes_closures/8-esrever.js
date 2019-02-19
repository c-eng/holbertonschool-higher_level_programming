#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let out = [];
  for (; i < list.length; i++) {
    out.push(list[list.length - (i + 1)]);
  }
  return out;
};
