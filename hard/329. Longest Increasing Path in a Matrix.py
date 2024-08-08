# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        memo = {}
        result = 1
        
        y_dir = [0, 1, 0, -1]
        x_dir = [1, 0, -1, 0]

        def is_inside(y, x):
            return (0 <= y < m and 0 <= x < n)
        
        def func(row, col):
            key = (row, col)
            if key in memo:
                return memo[key]
            res = 1
            for i in range(4):
                r, c = row + y_dir[i], col + x_dir[i]
                if is_inside(r, c) and matrix[r][c] > matrix[row][col]:
                    res = max(res, func(r, c) + 1)
            memo[key] = res
            return res
        
        for i in range(m):
            for j in range(n):
                result = max(result, func(i, j))
        
        return result
                