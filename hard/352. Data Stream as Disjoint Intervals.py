# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

# Implement the SummaryRanges class:

# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

# Example 1:

# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

from typing import List

class SummaryRanges:

    def __init__(self):
        self.stream = []
        

    def addNum(self, value: int) -> None:
        if not self.stream or self.stream[-1][1] < value:
            self.stream.append([value, value])
            return
        pos = self._get_pos(value)
        self.stream.insert(pos, [value, value])
        return
                
    def getIntervals(self) -> List[List[int]]:
        for i in range(len(self.stream) - 1, 0, -1):
            if self.stream[i][0] == self.stream[i - 1][1] + 1:
               self.stream[i - 1][1] = self.stream[i][1]
               self.stream.pop(i)
            elif self.stream[i][0] <= self.stream[i - 1][1]:
                self.stream[i - 1][1] = max(self.stream[i][1], self.stream[i - 1][1])
                self.stream.pop(i)
        return self.stream 
    

    def _get_pos(self, val):
        left = 0
        right = len(self.stream) - 1
        while left < right:
            mid = (left + right) // 2
            if self.stream[mid][0] > val:
                right = mid
            else:
                left = mid + 1
        return right
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
