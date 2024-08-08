# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

from collections import defaultdict
import math
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        max_val = 0
        for i, [x1, y1] in enumerate(points):
            temp = defaultdict(int)
            for x2, y2 in points[i + 1:]:
                if x1 == x2 and y1 == y2:
                    continue
                dx, dy = x1 - x2, y1 - y2
                if dx == 0:
                    temp[0] += 1
                    continue
                if dx * dy < 0:
                    dec = True
                else:
                    dec = False
                dx, dy = abs(dx), abs(dy)
                gradient = math.gcd(dx, dy)
                dx //= gradient
                dy //= gradient
                if dec:
                    k = (-dx, dy)
                else:
                    k = (dx, dy)
                temp[k] += 1
            for key in temp:
                max_val = max(max_val, temp[key] + 1)
        return max_val
