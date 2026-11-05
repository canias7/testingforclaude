function greet(name) {
  return "Hello, " + name;
}

function farewell(name) {
  return "Bye, " + name;
}

function isEmail(s) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
}

module.exports = { greet, farewell, isEmail };
