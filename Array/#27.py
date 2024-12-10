class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # Pointer for the new position in nums
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]  # Copy element if it is not val
                i += 1
        return i  # i represents the new length of the array

# Example usage
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
new_length = solution.removeElement(nums, val)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [2, 2]
