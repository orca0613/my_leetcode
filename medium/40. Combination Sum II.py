# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        memo = {}
        result = []

        def comb(cur, remain, t):
            if t < 0:
                return 0 
            key = tuple(cur)
            if key in memo:
                return memo[key]
            if t == 0:
                memo[key] = 1
                result.append(cur)
                return 1
            n = 0
            for i in range(len(remain)):
                n += comb(cur + [remain[i]], remain[i + 1:], t - remain[i])
            memo[key] = n
            return n
        
        comb([], candidates, target)
        return result
