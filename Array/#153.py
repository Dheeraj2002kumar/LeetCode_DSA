class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If the mid element is greater than the high element,
            # the minimum is in the right part of the array
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # Otherwise, the minimum is in the left part (including mid)
                high = mid
        
        # When the loop ends, low == high, pointing to the minimum
        return nums[low]

nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))  # Output: 0