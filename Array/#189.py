class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # To handle cases where k > n

        # Step 1: Reverse the entire array
        self.reverse(nums, 0, n - 1)

        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Step 3: Reverse the remaining n - k elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        """
        Reverse the elements in nums from index start to end.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# Example usage
solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
