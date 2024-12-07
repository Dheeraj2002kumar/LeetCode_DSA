class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            # Fill in the interior values of the row
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            # Add the completed row to the result
            result.append(row)

        return result

# Example usage
solution = Solution()
numRows = 5
print(solution.generate(numRows))
