# Given a string s, return whether s is a valid number.

# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# Formally, a valid number is defined using one of the following definitions:

# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.

# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

# The digits are defined as one or more digits.

 

# Example 1:

# Input: s = "0"

# Output: true

# Example 2:

# Input: s = "e"

# Output: false

# Example 3:

# Input: s = "."

# Output: false

class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == 1:
            return s.isdigit()
        
        operator = ["+", "-"]
        dot = 0
        
        def is_integer(num):
            c = None
            for char in num:
                if char.isdigit():
                    c = "digit"
                elif char in operator:
                    if c == None:
                        c = "op"
                    else:
                        return False
                else:
                    return False
            return c == "digit"
        
        def fucking(idx):
            if idx == 0:
                return s[1].isdigit()
            if idx == len(s) - 1:
                return s[idx - 1].isdigit()
            return s[idx - 1].isdigit() or s[idx + 1].isdigit()
            
        state = None
        
        e = ["e", "E"]
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                state = "digit"
            elif char in operator:
                if state == "e" or state == None:
                    state = "op"
                else:
                    return False
            elif char in e:
                if state == "digit" or state == "dot":
                    return is_integer(s[i + 1:])
                else:
                    return False
            elif char == ".":
                dot += 1
                if dot > 1:
                    return False
                if fucking(i):
                    state = "dot"
                else:
                    return False
            else:
                return False
        
        if state == "dot":
            return len(s) != 1
        else:
            return state == "digit"
                    
                    
        
        
        
            
            
        
