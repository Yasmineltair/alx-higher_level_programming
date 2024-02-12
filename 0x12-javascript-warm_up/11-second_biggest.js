#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv.length === 3) {
  console.log(0);
} else {
  const arg = process.argv.sort();
  console.log(arg.reverse()[1]);
}
