# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def cut_tail(a, b):
            la, lb = len(a), len(b)
            while a and b:
                if a[-1] == b[-1] or b[-1] == ".":
                    la -= 1
                    lb -= 1
                    a = a[:la]
                    b = b[:lb]
                elif b[-1] == "*":
                    return (a, b)
                else:
                    return False
            return (a, b)
        
        def match(A, B):
            t = cut_tail(A, B)
            if not t:
                return False
            a, b = t[0], t[1]
            if not b:
                return a == ""
            if not a:
                for i in range(1, len(b), 2):
                    if b[i] != "*":
                        return False
                return len(b) % 2 == 0
            if len(b) == 1:
                return False
            c = b[-2]
            t = b[:-2]
            r = match(a, t)
            if c == ".":
                for i in range(0, len(a) + 1):
                    r = r or match(a[:i], t)
            else:
                for i in range(len(a) - 1, -1, -1):
                    if a[i] == c:
                        r = r or match(a[:i], t)
                    else:
                        break
            return r
        
        return match(s, p)
                
            