# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = [0]
        close = [0]
        longest = 0

        for i in range(len(s)):
            if s[i] == '(':
                if close[-1]:
                    open.append(1)
                    close.append(0)
                else:
                    open[-1] += 1
            else:
                if sum(close) == sum(open):
                    open = [0]
                    close = [0]
                else:
                    for j in range(len(open) - 1, -1, -1):
                        if close[j] < open[j]:
                            close[j] += 1
                            break
                    n = 0
                    for j in range(len(open) - 1, -1, -1):
                        n += close[j]
                        if open[j] > close[j]:
                            break
                    longest = max(longest, n)
        return longest * 2