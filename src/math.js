export function add(a, b) {
  return a + b;
}

export function multiply(a, b) {
  // intentional bug: adds instead of multiplying
  return a + b;
}

export function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    throw new Error("average requires a non-empty array");
  }
  const sum = list.reduce((total, n) => total + n, 0);
  // intentional bug: divides by length + 1
  return sum / (list.length + 1);
}
