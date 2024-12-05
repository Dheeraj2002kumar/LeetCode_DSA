# Contains Duplicate (LeetCode #217)

class Solution:
  def containsDuplicate(self, nums):
    # initialize an empty set to track seen numbers
    seen = set()

    # Iterate through  each number in the list
    for num in nums:
       # If the number is already in the set, we found a duplicate 
       if num in seen:
          return True
       # Otherwise, add the number to the set
       seen.add(num)

    # If no duplicates were found, return False
    return False
  
# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    
    print(solution.containsDuplicate(nums1))  # Output: True
    print(solution.containsDuplicate(nums2))  # Output: False
    print(solution.containsDuplicate(nums3))  # Output: True



# +++++++++++ Complexity ++++++++++++++

# Time cmplexity: O(n)
# Iterating through the list takes linear time, and set operations (add and in) are average O(1)


# Space Complexity: O(n)
# In the worst case, the set will contain all n elements from the list if there are no duplicates.

