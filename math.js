// Returns the sum of two finite numbers, or throws.
export function add(a, b) {
  if (!Number.isFinite(a) || !Number.isFinite(b)) {
    throw new TypeError('add() requires two finite numbers');
  }
  return a + b;
}
