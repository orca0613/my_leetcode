# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        def get_odd_pal(idx):
            l = idx - 1
            r = idx + 1
            while 0 <= l and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l + 1:r]
        
        def get_even_pal(idx):
            l = idx
            r = idx + 1
            while 0 <= l and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l + 1:r]
        
        result = ""
        for i in range(len(s)):
            odd = get_odd_pal(i)
            even = get_even_pal(i)
            result = max(result, odd, even, key=lambda x: len(x))
        return result
            
        