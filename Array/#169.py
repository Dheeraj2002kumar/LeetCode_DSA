from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    
    print(solution.majorityElement(nums1))  # Output: 3
    print(solution.majorityElement(nums2))  # Output: 2
