function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

function average(list) {
  const sum = list.reduce((acc, n) => acc + n, 0);
  return sum / list.length;
}

module.exports = { add, multiply, average };
