/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let candidate = null;
  let count = 0;

  // Boyer-Moore Voting Algorithm
  for (let num of nums) {
      if (count === 0) {
          candidate = num; // Assign new candidate
      }
      count += (num === candidate) ? 1 : -1; // Increment or decrement count
  }

  return candidate;
};

// Example usage
const nums1 = [3, 2, 3];
const nums2 = [2, 2, 1, 1, 1, 2, 2];

console.log(majorityElement(nums1)); // Output: 3
console.log(majorityElement(nums2)); // Output: 2
