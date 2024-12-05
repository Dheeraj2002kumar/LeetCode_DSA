/**
 * @param {number} n
 * @return {Function}
 */
var createCounter = function(n) {
  let count = n; // Initialize the counter at n

  // Return a function that increments and returns the current value
  return function() {
      return count++;
  };
};

// Example Usage
const counter = createCounter(10);
console.log(counter()); // Output: 10
console.log(counter()); // Output: 11
console.log(counter()); // Output: 12
