/**
 * @param {Function} fn - The function to execute
 * @param {Array} args - Arguments to pass to the function
 * @param {number} t - Interval in milliseconds
 * @return {Function} - A function to cancel the interval
 */
var cancellable = function (fn, args, t) {
    // Execute the function immediately
    fn(...args);

    // Set up the interval to execute the function repeatedly
    const intervalId = setInterval(() => {
        fn(...args);
    }, t);

    // Return a function to cancel the interval
    return () => clearInterval(intervalId);
};

/**
 * Example Usage:
 * const result = [];
 * const fn = (x) => x * 2;
 * const args = [4], t = 35, cancelTimeMs = 190;
 * const start = performance.now();
 * const log = (...argsArr) => {
 *     const diff = Math.floor(performance.now() - start);
 *     result.push({"time": diff, "returned": fn(...argsArr)});
 * }
 * const cancel = cancellable(log, args, t);
 * setTimeout(cancel, cancelTimeMs);
 * setTimeout(() => {
 *     console.log(result);
 * }, cancelTimeMs + t + 15);
 */
