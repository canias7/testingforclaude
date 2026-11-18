export function add(a, b) {
  return a + b;
}

// Bug on purpose: adds instead of multiplying.
export function multiply(a, b) {
  return a + b;
}

// Bug on purpose: divides by one more than the list length.
export function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    throw new Error("average requires a non-empty list");
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / (list.length + 1);
}
