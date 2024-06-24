# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def parentheses(s, o, c):
            if o + c == 0:
                result.append(s)
                return
            if o == 0:
                return parentheses(s + ')', o, c - 1)
            parentheses(s + '(', o - 1, c)
            if o < c:
                parentheses(s + ')', o, c - 1)
        
        
        parentheses('', n, n)
        
        return result