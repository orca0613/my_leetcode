# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        matrix.append([None] * n)
        for i in range(m + 1):
            matrix[i].append(None)
        y_dir = [0, 1, 0, -1]
        x_dir = [1, 0, -1, 0]
        idx = 0
        result = []
        y = 0
        x = 0
        
        while matrix[y][x] != None:
            result.append(matrix[y][x])
            matrix[y][x] = None
            if matrix[y + y_dir[idx]][x + x_dir[idx]] == None:
                idx = (idx + 1) % 4
            y += y_dir[idx]
            x += x_dir[idx]
        return result
        
        
        