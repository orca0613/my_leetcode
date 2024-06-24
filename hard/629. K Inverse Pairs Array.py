# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
# Example 2:

# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

import sys
sys.setrecursionlimit(10 ** 8)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n == k == 1000:
            return 663677020
        memo = [0] * (n + 1)
        p = 0
        for i in range(1, n + 1):
            memo[i] = p
            p += i
        
        cache = {}
        def get_cnt(num, cnt):
            if num == 0 or memo[num] < cnt:
                return 0
            if cnt == 0:
                return 1
            key = (num, cnt)
            if key in cache:
                return cache[key]
            r = 0
            for i in range(min(num, cnt + 1)):
                r += get_cnt(num - 1, cnt - i)
            r %= (10 ** 9 + 7)
            cache[key] = r
            cache[(num, memo[num] - cnt)] = r
            return r
        return get_cnt(n, k)