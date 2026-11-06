import test from 'node:test';
import assert from 'node:assert/strict';
import { add } from './math.js';

test('add sums two numbers', () => {
  assert.equal(add(1, 2), 3);
  assert.equal(add(-1, 1), 0);
  assert.equal(add(1.5, 2.5), 4);
});

test('add rejects non-numbers', () => {
  assert.throws(() => add('1', '2'), TypeError);
  assert.throws(() => add(1, '2'), TypeError);
  assert.throws(() => add(null, 1), TypeError);
  assert.throws(() => add(NaN, 1), TypeError);
  assert.throws(() => add(Infinity, 1), TypeError);
});

test('add rejects missing arguments', () => {
  assert.throws(() => add(), TypeError);
  assert.throws(() => add(1), TypeError);
});
