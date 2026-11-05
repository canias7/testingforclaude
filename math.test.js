const test = require("node:test");
const assert = require("node:assert/strict");
const { double } = require("./math.js");

test("double(2) is 4", () => {
  assert.equal(double(2), 4);
});
