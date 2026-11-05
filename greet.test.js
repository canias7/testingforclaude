const { test } = require("node:test");
const assert = require("node:assert/strict");
const { greet, farewell, isEmail } = require("./greet");

test("greet returns Hello plus the name", () => {
  assert.equal(greet("Ada"), "Hello, Ada");
});

test("greet concatenates whatever name it is given", () => {
  assert.equal(greet(""), "Hello, ");
  assert.equal(greet("world"), "Hello, world");
});

test("farewell returns Bye plus the name", () => {
  assert.equal(farewell("Ada"), "Bye, Ada");
});

test("isEmail accepts a simple address and rejects junk", () => {
  assert.equal(isEmail("ada@example.com"), true);
  assert.equal(isEmail("not-an-email"), false);
  assert.equal(isEmail("a@b"), false);
});
