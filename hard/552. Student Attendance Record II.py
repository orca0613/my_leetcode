# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

# Example 1:

# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
# Example 2:

# Input: n = 1
# Output: 3
# Example 3:

# Input: n = 10101
# Output: 183236316

class Solution:
    def checkRecord(self, n: int) -> int:
        
        divider = 10 ** 9 + 7
        
        storage = [0] * 6
        
        memo = [
            [0, 1, 3],
            [0, 2, 3],
            [0, 3],
            [3, 4],
            [3, 5],
            [3]
        ]
            
        storage[0] = 1
        storage[1] = 1
        storage[3] = 1
        
        for i in range(n - 1):
            t = [0] * 6
            for j in range(6):
                for k in memo[j]:
                    t[k] += storage[j] % divider
                
            storage = t
        
        return sum(storage) % divider
        