import { test } from "node:test";
import assert from "node:assert/strict";
import { add, multiply } from "../src/math.js";
import { average } from "../src/stats.js";

test("add returns the sum of two numbers", () => {
  assert.equal(add(2, 3), 5);
  assert.equal(add(-1, 1), 0);
  assert.equal(add(0, 0), 0);
});

test("multiply returns the product of two numbers", () => {
  assert.equal(multiply(2, 3), 6);
  assert.equal(multiply(-4, 5), -20);
  assert.equal(multiply(0, 7), 0);
});

test("average returns the mean of a non-empty list", () => {
  assert.equal(average([2, 4, 6]), 4);
  assert.equal(average([10]), 10);
  assert.equal(average([1, 2, 3, 4]), 2.5);
});

test("average of an empty list is 0", () => {
  assert.equal(average([]), 0);
});
