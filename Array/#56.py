from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals based on the start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []  # This will store the merged intervals

        # Step 2: Iterate through the sorted intervals
        for interval in intervals:
            # If merged is empty or no overlap with the last interval in merged, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap exists; merge intervals by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# Example usage
if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(intervals))  # Output: [[1,6],[8,10],[15,18]]
