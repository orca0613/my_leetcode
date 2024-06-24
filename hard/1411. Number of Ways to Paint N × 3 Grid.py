# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

# Example 1:


# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.
# Example 2:

# Input: n = 5000
# Output: 30228214

class Solution:
    def numOfWays(self, n: int) -> int:
        if n == 1:
            return 12
        
        ret = 0
        cells = [
            (1, 2, 1), (2, 1, 2), (3, 1, 2),
            (1, 2, 3), (2, 1, 3), (3, 1, 3),
            (1, 3, 1), (2, 3, 1), (3, 2, 1),
            (1, 3, 2), (2, 3, 2), (3, 2, 3)
        ]
        
        memo = {}
        
        def painting(level, top, bottom):
            for i in range(3):
                if top[i] == bottom[i]:
                    return 0
                
            if level == 0:
                return 1
            
            key = (level, bottom)
            if key in memo:
                return memo[key]
            
            r = 0
            for i in range(12):
                r += painting(level - 1, bottom, cells[i])
            
            memo[key] = r
            return r
        
        for i in range(12):
            ret += painting(n - 1, (0, 0, 0), cells[i])
        
        return ret % (10 ** 9 + 7)
            