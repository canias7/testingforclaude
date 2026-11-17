function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    throw new Error("average requires a non-empty array");
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / list.length;
}

module.exports = { add, multiply, average };
