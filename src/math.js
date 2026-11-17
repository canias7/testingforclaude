export function add(a, b) {
  return a + b;
}

// Bug on purpose: returns a sum instead of a product.
export function multiply(a, b) {
  return a + b;
}

// Bug on purpose: divides by length + 1.
export function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    throw new Error("average requires a non-empty array");
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / (list.length + 1);
}
