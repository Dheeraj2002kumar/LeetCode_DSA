class Solution:
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            # Add the first row to the result
            result += matrix.pop(0)
            
            # Add the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            
            # Add the last row in reverse order
            if matrix:
                result += matrix.pop()[::-1]
            
            # Add the first element of each remaining row in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        return result


solution = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(solution.spiralOrder(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
