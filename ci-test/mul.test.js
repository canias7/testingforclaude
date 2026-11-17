const test = require("node:test");
const assert = require("node:assert/strict");
const { mul } = require("./mul.js");

test("mul(3, 4) is 12", () => {
  assert.equal(mul(3, 4), 12);
});
