/**
 * @param {Function} fn
 * @return {Function}
 */
var allowOneCall = function(fn) {
    let called = false;

    return function(...args) {
        if (!called) {
            called = true;
            return fn(...args);
        }
        return undefined;
    };
};

// Example usage:
const add = (a, b) => a + b;
const addOnce = allowOneCall(add);

console.log(addOnce(2, 3)); // Output: 5
console.log(addOnce(5, 7)); // Output: undefined
