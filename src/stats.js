function average(list) {
  if (list.length === 0) return 0;
  const sum = list.reduce((acc, n) => acc + n, 0);
  return sum / list.length;
}

module.exports = { average };
