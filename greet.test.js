const { test } = require("node:test");
const assert = require("node:assert/strict");
const { greet } = require("./greet");

test("greet returns Hello plus the name", () => {
  assert.equal(greet("Ada"), "Hello, Ada");
});

test("greet concatenates whatever name it is given", () => {
  assert.equal(greet(""), "Hello, ");
  assert.equal(greet("world"), "Hello, world");
});
