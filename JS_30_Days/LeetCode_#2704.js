/**
 * @param {any} val
 * @return {Object}
 */
var expect = function(val) {
  return {
      toBe: function(expected) {
          if (val === expected) {
              return true;
          } else {
              throw new Error("Not Equal");
          }
      },
      notToBe: function(expected) {
          if (val !== expected) {
              return true;
          } else {
              throw new Error("Equal");
          }
      }
  };
};

// Example usage
const result1 = expect(5).toBe(5); // true
console.log(result1);

const result2 = expect(5).notToBe(10); // true
console.log(result2);

try {
  expect(5).toBe(10); // Throws Error: "Not Equal"
} catch (error) {
  console.error(error.message);
}

try {
  expect(5).notToBe(5); // Throws Error: "Equal"
} catch (error) {
  console.error(error.message);
}
