/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
  // Return a new promise
  return new Promise((resolve, reject) => {
    // Use an array to hold the results of each promise
    let results = [];
    let completed = 0;

    // Loop over the functions array
    functions.forEach((func, index) => {
      // Call the function to get the promise
      func().then(result => {
        // Store the result in the results array
        results[index] = result;
        completed++;

        // If all promises have been resolved, resolve the main promise with the results array
        if (completed === functions.length) {
          resolve(results);
        }
      }).catch(err => {
        // If any promise rejects, reject the main promise with the error
        reject(err);
      });
    });
  });
};

/**
 * Example usage:
 * const promise = promiseAll([() => new Promise(res => res(42)), () => new Promise(res => res(36))]);
 * promise.then(console.log); // [42, 36]
 */
