#!/usr/bin/node
function frac (a) {
  if ((isNaN(a)) || (a === 1)) {
    return 1;
  } else {
    return a * frac(a - 1);
  }
}
console.log(frac(parseInt(process.argv[2])));
