# A password is considered strong if the below conditions are all met:

# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
# Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

# In one step, you can:

# Insert one character to password,
# Delete one character from password, or
# Replace one character of password with another character.
 

# Example 1:

# Input: password = "a"
# Output: 5
# Example 2:

# Input: password = "aA1"
# Output: 3
# Example 3:

# Input: password = "1337C0d3"
# Output: 0

import re
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        def erase(s):
            l = []
            left = 1
            n = 0
            h = max(len(password) - 20, 0)
            for i in range(1, len(s)):
                if s[i].isalpha():
                    num = int(s[left:i])
                    left = i + 1
                    if num >= 3:
                        l.append(num)
            num = int(s[left:len(s)])
            if num >= 3:
                l.append(num)
            l.sort(key=lambda x: x % 3)
            for i in range(len(l)):
                g = l[i] % 3
                if g < h:
                    l[i] -= (g + 1)
                    h -= (g + 1)
                n += l[i] // 3
            return max(n - (h // 3), 0)
        
        def filt(s):
            return len(set(re.sub(r'[0-9t]', '', s)))
        
        def modify(s, w):
            if not w:
                return s
            c = w[0]
            if c.isdigit():
                d = 'n'
            elif c.isalpha():
                if ord(c) > 96:
                    d = 'l'
                else:
                    d = 'u'
            else:
                d = 't'
            s += d
            for i in range(1, len(w)):
                if w[i] != c:
                    s += str(i)
                    return modify(s, w[i:])
            return s + str(len(w))
        
        result = 0
        n = max(6 - len(password), 0)
        m = modify('', password)
        e = max(erase(m), n)
        result += e
        f = filt(m)
        result += max(3 - f - e, 0)
        result += max(len(password) - 20, 0)
        return result
        
        
        