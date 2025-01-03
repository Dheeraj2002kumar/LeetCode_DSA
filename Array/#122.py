class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

# Example usage
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7
print(solution.maxProfit([1, 2, 3, 4, 5]))     # Output: 4
print(solution.maxProfit([7, 6, 4, 3, 1]))     # Output: 0
