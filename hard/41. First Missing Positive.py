# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        memo = [True] * (length + 2)
        for num in nums:
            if num > 0 and num <= length:
                memo[num] = False
        for i in range(1, len(memo)):
            if memo[i]:
                return i