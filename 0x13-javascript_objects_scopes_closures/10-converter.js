#!/usr/bin/node
exports.converter = function (base) {
  function ownConverter (num) {
    return num.toString(base);
  }
  return ownConverter;
};
