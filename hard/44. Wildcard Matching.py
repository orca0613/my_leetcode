# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        al_q = 0
                
        while p and s and p[-1].isalpha():
            if p[-1] != s[-1]:
                return False
            p = p[:-1]
            s = s[:-1]
            
        for char in p:
            if char.isalpha() or char == "?":
                al_q += 1
        
        def matching(a, b, n):
            if len(b) == 0:
                return len(a) == 0
            if len(a) == 0:
                return n == 0
            if a[0] == b[0] or b[0] == "?":
                return matching(a[1:], b[1:], n - 1)
            if b[0] != "*":
                return False
            key = (a, b)
            if key in cache:
                return cache[key]
            r = False
            l = len(a)
            for i in range(l - n, -1, -1):
                r = r or matching(a[i:l], b[1:], n)

            cache[key] = r
            return r
        
        return matching(s, p, al_q)
            