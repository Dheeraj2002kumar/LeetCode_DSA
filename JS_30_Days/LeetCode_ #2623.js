function memoize(fn) {
    const cache = new Map();

    return function (...args) {
        const key = JSON.stringify(args); // Create a unique key based on arguments
        if (cache.has(key)) {
            return cache.get(key); // Return cached result if available
        }
        const result = fn(...args); // Compute the result otherwise
        cache.set(key, result); // Cache the result
        return result;
    };
}

// Example usage
const add = (a, b) => a + b;
const memoizedAdd = memoize(add);

console.log(memoizedAdd(1, 2)); // 3 (computed)
console.log(memoizedAdd(1, 2)); // 3 (cached)
console.log(memoizedAdd(2, 3)); // 5 (computed)
