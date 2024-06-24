# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lt = len(t)
        ls = len(s)
        
        cache = {}
        
        def get_cnt(idx1, idx2):
            if idx2 == lt:
                return 1
            if idx1 == ls:
                return 0
            if ls - idx1 < lt - idx2:
                return 0
            key = (idx1, idx2)
            if key in cache:
                return cache[key]
            r = 0
            for i in range(idx1, ls):
                if s[i] == t[idx2]:
                    r += get_cnt(i + 1, idx2 + 1)
            cache[key] = r
            return r
        
        return get_cnt(0, 0)
        