# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        result[0][0] = 1
        i = 0
        j = 1
        r_b = [n - 1, n - 1]
        l_t = [1, 0]
        right = True
        cur = 2
        while cur <= n ** 2:
            result[i][j] = cur
            cur += 1
            if i == l_t[0] and j == l_t[1]:
                right = True
                l_t[0] += 1
                l_t[1] += 1
            elif i == r_b[0] and j == r_b[1]:
                right = False
                r_b[0] -= 1
                r_b[1] -= 1
            if right:
                if j < r_b[1]:
                    j += 1
                else:
                    i += 1
            else:
                if j > l_t[1]:
                    j -= 1
                else:
                    i -= 1
                    
        return result
            
            