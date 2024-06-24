# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

# Example 1:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
# Example 2:

# Input: grid = [[7]]
# Output: 7

from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        table = []
        
        
        for i in range(m):
            s = sorted(grid[i])[:3]
            table.append(set(s))
        
        memo = {}
        answer = float("inf")
        
        def get_sum(y, x):
            if grid[y][x] not in table[y]:
                return float("inf")
            if y == m - 1:
                return grid[y][x]
            key = (y, x)
            if key in memo:
                return memo[key]
            
            r = float("inf")
            for i in range(n):
                if i == x:
                    continue
                r = min(r, get_sum(y + 1, i))
            r += grid[y][x]
            memo[key] = r
            return r
        
        for i in range(n):
            answer = min(answer, get_sum(0, i))
        return answer
            
                
            
        