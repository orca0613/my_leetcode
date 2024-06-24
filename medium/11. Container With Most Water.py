# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left = height[l]
        right = height[r]
        result = 0
        
        while l < r:
            result = max(min(left, right) * (r - l), result)
            if left < right:
                while height[l] <= left and l < len(height):
                    l += 1
                left = height[l]
            else:
                while height[r] <= right and r > 0:
                    r -= 1
                right = height[r]
            
        return result
        