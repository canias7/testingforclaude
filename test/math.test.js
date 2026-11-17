const { describe, it } = require("node:test");
const assert = require("node:assert/strict");
const { add, multiply } = require("../src/math");
const { average } = require("../src/stats");

describe("add", () => {
  it("adds two numbers", () => {
    assert.equal(add(2, 3), 5);
  });

  it("adds negatives", () => {
    assert.equal(add(-1, 4), 3);
  });
});

describe("multiply", () => {
  it("multiplies two numbers", () => {
    assert.equal(multiply(2, 3), 6);
  });

  it("multiplies by zero", () => {
    assert.equal(multiply(5, 0), 0);
  });
});

describe("average", () => {
  it("averages a list of numbers", () => {
    assert.equal(average([2, 4, 6]), 4);
  });

  it("averages a single value", () => {
    assert.equal(average([10]), 10);
  });

  it("returns 0 for an empty list", () => {
    assert.equal(average([]), 0);
  });
});
