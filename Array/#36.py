class Solution:
    def searchInsert(self, nums, target):
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found, return its index
            
            # If the target is greater than the middle element
            elif nums[mid] < target:
                left = mid + 1  # Move the left pointer to search the right half
            
            # If the target is less than the middle element
            else:
                right = mid - 1  # Move the right pointer to search the left half
        
        # If the target is not found, 'left' is the insertion position
        return left


solution = Solution()
nums = [1, 3, 5, 6]
target = 2
print(solution.searchInsert(nums, target))  # Output: 1
