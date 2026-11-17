const test = require('node:test');
const assert = require('node:assert/strict');
const { average } = require('../src/stats');

test('average', () => {
  assert.equal(average([2, 4, 6]), 4);
  assert.equal(average([10]), 10);
});

test('average of empty list is 0', () => {
  assert.equal(average([]), 0);
});
