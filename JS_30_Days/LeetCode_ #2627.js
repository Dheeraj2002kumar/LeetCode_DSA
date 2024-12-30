/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
  let timeout; // Variable to store the timeout ID

  return function (...args) {
    clearTimeout(timeout); // Clear any previously set timeout
    timeout = setTimeout(() => fn(...args), t); // Set a new timeout to call the function
  };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // Cancelled
 * log('Hello'); // Cancelled
 * log('Hello'); // Logged at t=100ms
 */
