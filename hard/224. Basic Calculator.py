# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        print(s)
        def cal(monomial):
            num = 0
            cur = "0"
            add = True
            for char in monomial:
                if char.isdigit():
                    cur += char
                elif char == "+":
                    if add:
                        num += int(cur)
                    else:
                        num -= int(cur)
                    add = True
                    cur = "0"
                elif char == "-":
                    if add:
                        num += int(cur)
                    else:
                        num -= int(cur)
                    add = cur == "0" and not add
                    cur = "0"
            if add:
                num += int(cur)
            else:
                num -= int(cur)
            return str(num)
        
        memo = []
        idx = 0
        while idx < len(s):
            if s[idx] == "(":
                memo.append(idx)
            elif s[idx] == ")":
                start = memo.pop()
                piece = s[start + 1:idx]
                s = s[:start] + cal(piece) + s[idx + 1:]
                idx = start
            idx += 1
        return int(cal(s))
                
test = Solution()
print(test.calculate("1-(     -2)"))
