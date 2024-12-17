/**
 * @return {number}
 */
var argumentsLength = function (...args) {
    return args.length;
};

// Example usage
console.log(argumentsLength(1, 2, 3)); // Output: 3
console.log(argumentsLength());        // Output: 0
console.log(argumentsLength(10));      // Output: 1
