class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize the closest sum to infinity
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Use two pointers
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                # Update closest_sum if the current sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:  # If the current sum equals the target, return immediately
                    return current_sum
        
        return closest_sum


solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(solution.threeSumClosest(nums, target))  # Output: 2
