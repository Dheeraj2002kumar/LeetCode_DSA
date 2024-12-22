from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given n x n matrix 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap elements across the diagonal (i, j) with (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

# Example usage
if __name__ == "__main__":
    # Example input matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the rotate method
    solution.rotate(matrix)
    
    # Print the rotated matrix
    print("Rotated matrix:")
    for row in matrix:
        print(row)
