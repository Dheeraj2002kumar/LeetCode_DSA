function reduce(nums, fn, initialValue) {
    let accumulator = initialValue;

    for (let i = 0; i < nums.length; i++) {
        accumulator = fn(accumulator, nums[i]);
    }

    return accumulator;
}

// Example usage:
const nums = [1, 2, 3, 4];
const sumFn = (acc, curr) => acc + curr;
const result = reduce(nums, sumFn, 0); // Output: 10
console.log(result);
