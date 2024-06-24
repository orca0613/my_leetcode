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
        if not self.stream:
            self.stream.append([value, value])
        else:
            for i in range(len(self.stream)):
                if self.stream[i][0] > value:
                    self.stream.insert(i, [value, value])
                    return
            self.stream.append([value, value])
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


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()