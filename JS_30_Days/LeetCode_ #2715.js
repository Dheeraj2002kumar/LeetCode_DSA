/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
    // Set up a timeout that will execute the function `fn` after `t` milliseconds
    let timeoutId;

    // Create the cancel function to clear the timeout
    const cancelFn = () => clearTimeout(timeoutId);

    // Set the timeout to execute the function `fn` with the provided arguments after `t` milliseconds
    timeoutId = setTimeout(() => {
        fn(...args); // Execute the function `fn` with the arguments `args`
    }, t);

    // Return the cancel function that can be called to prevent the function execution
    return cancelFn;
};

/**
 * Example usage:
 */

// Array to store the results
const result = [];

// Example function to multiply by 5
const fn = (x) => x * 5;

// Arguments to pass to the function
const args = [2];

// Time to execute the function (in milliseconds)
const t = 20;

// Time after which to cancel the execution
const cancelTimeMs = 50;

// Capture the start time for time logging
const start = performance.now();

// Function to log the time and result
const log = (...argsArr) => {
    const diff = Math.floor(performance.now() - start); // Calculate the elapsed time
    result.push({ "time": diff, "returned": fn(...argsArr) }); // Push the result with the time to the result array
};

// Call the cancellable function to create a cancel function
const cancel = cancellable(log, args, t);

// Calculate the maximum time to log the result
const maxT = Math.max(t, cancelTimeMs);

// Set a timeout to cancel the function execution after cancelTimeMs
setTimeout(cancel, cancelTimeMs);

// Set a timeout to log the result after the maximum time to ensure the function has been executed
setTimeout(() => {
    console.log(result); // Expected output: [{"time":20,"returned":10}]
}, maxT + 15);
