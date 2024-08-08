# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(reverse=True)
        cur = intervals.pop()
        while intervals:
            next_time = intervals.pop()
            if cur[1] >= next_time[0]:
                cur = [cur[0], max(cur[1], next_time[1])]
            else:
                answer.append(cur)
                cur = next_time
        answer.append(cur)
        return answer
        