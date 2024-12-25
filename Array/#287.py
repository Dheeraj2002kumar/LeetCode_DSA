def findDuplicate(nums):
    # Phase 1: Use Floyd's Tortoise and Hare to find the intersection point
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]  # Move slow pointer by 1 step
        fast = nums[nums[fast]]  # Move fast pointer by 2 steps
        if slow == fast:  # They meet at some point
            break

    # Phase 2: Find the entrance to the cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]  # Move both pointers by 1 step
        fast = nums[fast]
    
    return slow

# Example usage
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
