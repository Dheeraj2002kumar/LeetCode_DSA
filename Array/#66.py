class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):  # Start iterating from the last digit
            if digits[i] < 9:  # If the digit is less than 9, just increment and return
                digits[i] += 1
                return digits
            digits[i] = 0  # If the digit is 9, it becomes 0 and carry propagates
        
        # If all digits are 0, we have a carry that creates a new leading 1
        return [1] + digits

# Example usage
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
