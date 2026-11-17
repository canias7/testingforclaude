function average(list) {
  if (!Array.isArray(list) || list.length === 0) {
    return 0;
  }
  const sum = list.reduce((total, n) => total + n, 0);
  return sum / list.length;
}

module.exports = { average };
