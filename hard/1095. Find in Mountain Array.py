# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr) -> int: # mountain_arr: MountainArray
        if mountain_arr.get(0) == target:
            return 0
        left = 0
        right = mountain_arr.length()
        result = -1
        while right - left > 2:
            n = (right - left) // 3
            l = left + n
            r = right - n
            if mountain_arr.get(l) > mountain_arr.get(r):
                right = r
                pick = l
            else:
                left = l
                pick = r
        
        def inc(l, r):
            if r <= l + 1:
                return -1
            mid = (l + r) // 2
            m = mountain_arr.get(mid)
            if m == target:
                return mid
            elif m < target:
                return inc(mid, r)
            else:
                return inc(l, mid)
            
        def dec(l, r):
            if r <= l + 1:
                return -1
            mid = (l + r) // 2
            m = mountain_arr.get(mid)
            if m == target:
                return mid
            elif m > target:
                return dec(mid, r)
            else:
                return dec(l, mid)

        p = mountain_arr.get(pick)
        if p == target:
            return pick
        elif p < target:
            return -1
        if mountain_arr.get(0) < target:
            result = inc(0, pick)
            if result > 0:
                return result
        if mountain_arr.get(mountain_arr.length() - 1) == target:
            return mountain_arr.length() - 1
        result = dec(pick, mountain_arr.length() - 1)
        return result
        
        
                
        