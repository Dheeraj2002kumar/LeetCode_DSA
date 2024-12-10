/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const result = []; // Initialize an empty array to store the transformed elements
    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i)); // Apply the function and store the result
    }
    return result; // Return the transformed array
};

// Example Usage:
const arr = [1, 2, 3];
const fn = function(n, i) { return n * 2 + i; };
console.log(map(arr, fn)); // Output: [2, 5, 8]
