export function add(a, b) {
  return a + b;
}

export function multiply(a, b) {
  return a * b;
}

export function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    throw new Error("average requires a non-empty list");
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / list.length;
}
