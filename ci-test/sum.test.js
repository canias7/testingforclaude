const { test } = require("node:test");
const assert = require("node:assert/strict");
const { sum } = require("./sum");

test("sum(2, 3) is 5", () => {
  assert.equal(sum(2, 3), 5);
});

test("sum(-1, 1) is 0", () => {
  assert.equal(sum(-1, 1), 0);
});
