class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Calculate the maximum area of water a container can store.

        :param height: List of integers representing heights of lines.
        :return: Integer representing the maximum area of water.
        """
        # Initialize two pointers, one at the beginning and one at the end
        left, right = 0, len(height) - 1
        max_area = 0

        # Use the two-pointer technique
        while left < right:
            # Calculate the current area
            current_area = (right - left) * min(height[left], height[right])
            
            # Update the maximum area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage
if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Maximum Area:", solution.maxArea(height))
