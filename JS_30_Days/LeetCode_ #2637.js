/**
 * @param {Function} fn - The asynchronous function to be wrapped
 * @param {number} t - The time limit in milliseconds
 * @return {Function} - A function that enforces the time limit
 */
const timeLimit = (fn, t) => {
  return async (...args) => {
    // Create a timeout promise that rejects after `t` milliseconds
    const timeoutPromise = new Promise((_, reject) => {
      setTimeout(() => {
        reject("Time Limit Exceeded");
      }, t);
    });

    // Race the timeout promise against the actual function call
    return Promise.race([fn(...args), timeoutPromise]);
  };
};

// Example Usage
const exampleFunction = async (n) => {
  return new Promise((resolve) => setTimeout(() => resolve(n), n));
};

const limitedFunction = timeLimit(exampleFunction, 100);

limitedFunction(150)
  .then(console.log) // Will not resolve
  .catch(console.error); // "Time Limit Exceeded"
