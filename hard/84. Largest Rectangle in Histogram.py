# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def merge(left, right, size):
            l = len(left) - 1
            r = len(left)
            merged = left + right
            shortest = min(merged[l], merged[r])
            while True:
                while l > 0 and merged[l - 1] >= shortest:
                    l -= 1
                while r < len(merged) - 1 and merged[r + 1] >= shortest:
                    r += 1
                size = max(size, shortest * (r - l + 1))
                if l > 0 and r < len(merged) - 1:
                    shortest = max(merged[l - 1], merged[r + 1])
                elif l == 0 and r < len(merged) - 1:
                    shortest = merged[r + 1]
                elif l > 0 and r == len(merged) - 1:
                    shortest = merged[l - 1]
                else:
                    break
            return (merged, size)
                
        def split(lst):
            if len(lst) == 1:
                return (lst, lst[0])
            else:
                pivot = len(lst) // 2
                l = split(lst[:pivot])
                r = split(lst[pivot:])
                return merge(l[0], r[0], max(l[1], r[1]))
        
        return split(heights)[1]
    
                
            
                    
                
            
        