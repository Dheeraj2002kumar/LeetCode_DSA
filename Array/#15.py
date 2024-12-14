class Solution:
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the input array
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach to find pairs that sum up to -nums[i]
            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # Increase the sum
                else:
                    right -= 1  # Decrease the sum

        return result

nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
