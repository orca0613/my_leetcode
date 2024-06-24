# 1. Two Sum
# Easy

# 56730

# 1970

# Add to List

# Share
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        special = []
        for i in range(len(nums)):
            if nums[i] * 2 == target:
                special.append(i)
            else:
                memo[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in memo:
                if memo[nums[i]] != i:
                    return [memo[nums[i]], i]
        return special