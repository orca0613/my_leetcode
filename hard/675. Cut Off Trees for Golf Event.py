# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

# Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

 

# Example 1:


# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
# Example 2:


# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
# Example 3:

# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the trees.
# Note that you can cut off the first tree at (0, 0) before making any steps.

from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        memo = []
        
        def is_movable(coord):
            y, x = coord[0], coord[1]
            return 0 <= y < m and 0 <= x < n and forest[y][x] > 0
        
        def get_neighbors(coord):
            y, x = coord[0], coord[1]
            return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        
        def find_shortest(cur, target):
            visited = set()
            stack = [cur]
            step = 0
            while True:
                temp = []
                while stack:
                    c = stack.pop()
                    if c == target:
                        return step
                    neighbors = get_neighbors(c)
                    for neighbor in neighbors:
                        if is_movable(neighbor) and neighbor not in visited:
                            visited.add(neighbor)
                            temp.append(neighbor)
                
                if len(temp) > 0:
                    step += 1
                    stack = temp
                else:
                    break
            return -1
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    memo.append((forest[i][j], i, j))
        
        memo.sort(reverse=True)
        result = 0
        current = (0, 0)
        while memo:
            t = memo.pop()
            target = (t[1], t[2])
            r = find_shortest(current, target)
            if r < 0:
                return -1
            result += r
            current = target
        return result
        
        
        
        
                    
            
        