class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculate the number of continuous subarrays that sum to k.
        """
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            current_sum += num
            
            # Check if there is a prefix sum that matches current_sum - k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            
            # Update the prefix sums map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count

# Example usage
solution = Solution()
nums = [1, 1, 1]
k = 2
print(solution.subarraySum(nums, k))  # Output: 2
