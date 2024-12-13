class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        # Initialize the answer array with 1s
        answer = [1] * n

        # Compute prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Compute postfix products and multiply with the prefix values
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer

nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
