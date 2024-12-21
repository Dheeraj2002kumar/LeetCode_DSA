/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
    try {
        const [value1, value2] = await Promise.all([promise1, promise2]);
        return value1 + value2;
    } catch (error) {
        throw error;
    }
};

// Example usage:
const promise1 = Promise.resolve(3);
const promise2 = Promise.resolve(5);

addTwoPromises(promise1, promise2).then(console.log); // Output: 8
