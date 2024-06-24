# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import defaultdict
import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        numbers = []
        memo = defaultdict(int)
        for i in range(k - 1):
            heapq.heappush(numbers, -nums[i])
            memo[nums[i]] += 1
        
        for i in range(k - 1, len(nums)):
            memo[nums[i]] += 1
            heapq.heappush(numbers, -nums[i])
            max_val = -numbers[0]
            while memo[max_val] == 0:
                heapq.heappop(numbers)
                max_val = -numbers[0]
            result.append(max_val)
            memo[nums[i - k + 1]] -= 1
            
        return result