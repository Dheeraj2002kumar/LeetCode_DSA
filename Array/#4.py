class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine the two arrays and sort them
        merged = sorted(nums1 + nums2)
        
        # Calculate the middle index
        n = len(merged)
        mid = n // 2
        
        # If the length is odd, return the middle element
        if n % 2 == 1:
            return merged[mid]
        
        # If the length is even, return the average of the two middle elements
        return (merged[mid - 1] + merged[mid]) / 2.0