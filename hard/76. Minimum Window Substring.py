# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memo = defaultdict(int)
        char_set = set(t)
        for char in t:
            memo[char] += 1
        result = s + "!"
        left = 0
        
        def window(l, cur, w):
            while l < len(s):
                a = s[l]
                memo[a] += 1
                if memo[a] > 0:
                    char_set.add(a)
                    sliced = s[l:cur + 1]
                    w = sliced if len(sliced) < len(w) else w
                    return (l + 1, w)
                l += 1
        
        for i, c in enumerate(s):
            memo[c] -= 1
            if not memo[c]:
                char_set.remove(c)
                if not char_set:
                    left, result = window(left, i, result)
        return result if len(result) <= len(s) else ""
    