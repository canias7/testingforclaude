export function average(list) {
  if (!Array.isArray(list)) {
    throw new Error("average requires a list");
  }
  if (list.length === 0) {
    return 0;
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / list.length;
}
