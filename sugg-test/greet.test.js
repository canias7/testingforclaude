const { describe, it } = require('node:test');
const assert = require('node:assert/strict');
const { greet } = require('./greet');

describe('greet', () => {
  it('returns Hello plus the name', () => {
    assert.equal(greet('Ada'), 'Hello, Ada');
  });
});
