# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

# Example 1:


# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0

from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix) + 1
        col = len(matrix[0]) + 1
        table = [[0] * col for _ in range(row)]
        result = 0
        for i in range(1, row):
            for j in range(1, col):
                table[i][j] = table[i - 1][j] + table[i][j - 1] + matrix[i - 1][j - 1] - table[i - 1][j - 1]
        
        def get_submat(y, x):
            r = 0
            p = table[y][x]
            for i in range(y):
                for j in range(x):
                    if p - table[y][j] - table[i][x] + table[i][j] == target:
                        r += 1
            return r
        
        for i in range(1, row):
            for j in range(1, col):
                result += get_submat(i, j)
        return result
                
        