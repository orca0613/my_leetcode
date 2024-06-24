# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

import heapq
class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []
    
    def __swap(self):
        m = heapq.heappop(self.min)
        M = heapq.heappop(self.max)
        heapq.heappush(self.max, -m)
        heapq.heappush(self.min, -M)

    def addNum(self, num: int) -> None:
        if len(self.max) == len(self.min):
            heapq.heappush(self.max, -num)
        else:
            heapq.heappush(self.min, num)
        if self.min and -(self.max[0]) > self.min[0]:
            self.__swap()

    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -(self.max[0])
        else:
            return (-(self.max[0]) + self.min[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()