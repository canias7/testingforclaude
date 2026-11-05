const test = require('node:test');
const assert = require('node:assert/strict');
const { capitalize } = require('./greet');

test('capitalize makes the first letter uppercase', () => {
  assert.equal(capitalize('hello'), 'Hello');
  assert.equal(capitalize('Hello'), 'Hello');
  assert.equal(capitalize('a'), 'A');
  assert.equal(capitalize(''), '');
});
