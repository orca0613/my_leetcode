# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        memo = {}
        answer = 0
        for line in grid:
            t = ""
            for num in line:
                t += str(num) + "-"
            if t in memo:
                memo[t] += 1
            else:
                memo[t] = 1
        
        for i in range(len(grid)):
            t = ""
            for j in range(len(grid)):
                t += str(grid[j][i]) + "-"
            if t in memo:
                answer += memo[t]
        return answer
                
                
            
        