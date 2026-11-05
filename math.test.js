import test from 'node:test';
import assert from 'node:assert/strict';
import { add } from './math.js';

test('add sums two numbers', () => {
  assert.equal(add(1, 2), 3);
  assert.equal(add(-1, 1), 0);
  assert.equal(add(1.5, 2.5), 4);
});

test('add concatenates strings with +', () => {
  assert.equal(add('1', '2'), '12');
});

test('add returns NaN when an argument is missing', () => {
  assert.equal(Number.isNaN(add()), true);
  assert.equal(Number.isNaN(add(1)), true);
});
