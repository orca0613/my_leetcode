# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        l_wall = height[0]
        r_wall = height[-1]
        
        answer = 0
        
        while left < right - 1:
            if l_wall < r_wall:
                left += 1
                n = height[left]
                answer += max(l_wall - n, 0)
                l_wall = max(l_wall, n)
            else:
                right -= 1
                n = height[right]
                answer += max(r_wall - n, 0)
                r_wall = max(r_wall, n)
                
        return answer