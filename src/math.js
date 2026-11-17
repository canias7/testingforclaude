function add(a, b) {
  return a + b;
}

// Intentional bug: returns a sum instead of a product.
function multiply(a, b) {
  return a + b;
}

// Intentional bug: divides by length + 1, so the mean is too small.
function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    throw new Error("average requires a non-empty array");
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / (list.length + 1);
}

module.exports = { add, multiply, average };
