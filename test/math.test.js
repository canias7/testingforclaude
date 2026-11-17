const test = require('node:test');
const assert = require('node:assert/strict');
const { add, multiply, average } = require('../src/math');

test('add', () => {
  assert.equal(add(2, 3), 5);
  assert.equal(add(-1, 1), 0);
});

test('multiply', () => {
  assert.equal(multiply(3, 4), 12);
  assert.equal(multiply(5, 0), 0);
});

test('average', () => {
  assert.equal(average([2, 4, 6]), 4);
  assert.equal(average([10]), 10);
});
