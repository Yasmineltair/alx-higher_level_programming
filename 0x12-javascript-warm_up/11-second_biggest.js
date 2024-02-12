#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arg = process.argv.sort();
  console.log(arg.reverse()[1]);
}
