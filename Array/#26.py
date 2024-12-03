class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Handle empty array
        
        i = 0  # Pointer for the last unique element
        for j in range(1, len(nums)):  # Start from the second element
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1  # Move pointer for unique elements
                nums[i] = nums[j]  # Update the array in-place
        
        return i + 1  # Number of unique elements



solution = Solution()
nums = [1, 1, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)
print(k)        
print(nums[:k])  
