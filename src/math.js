function add(a, b) {
  return a + b;
}

// BUG (intentional): should be a * b
function multiply(a, b) {
  return a + b;
}

// BUG (intentional): should divide by list.length
function average(list) {
  const sum = list.reduce((acc, n) => acc + n, 0);
  return sum / (list.length + 1);
}

module.exports = { add, multiply, average };
