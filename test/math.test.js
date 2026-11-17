const test = require('node:test');
const assert = require('node:assert/strict');
const { add, multiply } = require('../src/math');

test('add', () => {
  assert.equal(add(2, 3), 5);
  assert.equal(add(-1, 1), 0);
});

test('multiply', () => {
  assert.equal(multiply(3, 4), 12);
  assert.equal(multiply(5, 0), 0);
});
