# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

# Example 1:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:


# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        wall = set()
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    goal = (i, j)
                elif grid[i][j] == -1:
                    wall.add((i, j))
        empty = m * n - len(wall) - 2
        
        def is_inside(y, x):
            return (0 <= y < m and 0 <= x < n)
            
        
        def path(y, x, v):
            nonlocal result
            t = (y, x)
            if not is_inside(y, x)  or (t in v) or (t in wall) or (t == start):
                return
            if t == goal:
                if len(v) == empty:
                    result += 1
                return
            path(y + 1, x, v | {t})
            path(y - 1, x, v | {t})
            path(y, x + 1, v | {t})
            path(y, x - 1, v | {t})
        
        path(start[0] + 1, start[1], set())
        path(start[0] - 1, start[1], set())
        path(start[0], start[1] + 1, set())
        path(start[0], start[1] - 1, set())
        
        return result
                
                
            
        