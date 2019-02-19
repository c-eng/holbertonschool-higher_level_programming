#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;
  for (; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
