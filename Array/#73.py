from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Step 1: Determine which rows and columns should be set to zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_zero = True
                    if c == 0:
                        first_col_zero = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Step 2: Use the markers to set the appropriate cells to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Step 3: Handle the first row
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        # Step 4: Handle the first column
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

# Example usage
if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    solution.setZeroes(matrix)
    print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
