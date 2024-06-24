# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float("inf")
        l = len(nums)
        if target > 0:
            nums.sort(reverse=True)
            for i in range(l):
                for j in range(i + 1, l):
                    for k in range(j + 1, l):
                        s = nums[i] + nums[j] + nums[k]
                        result = min(result, s, key=lambda x: abs(x - target))
                        if s <= target:
                            break
        else:
            nums.sort()  
            for i in range(l):
                for j in range(i + 1, l):
                    for k in range(j + 1, l):
                        s = nums[i] + nums[j] + nums[k]
                        result = min(result, s, key=lambda x: abs(x - target))
                        if s >= target:
                            break
        return result
        