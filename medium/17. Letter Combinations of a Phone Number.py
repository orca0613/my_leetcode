# 17. Letter Combinations of a Phone Number
# Medium

# 18453

# 993

# Add to List

# Share
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        table = []
        n = 97
        for i in range(8):
            table.append([])
            for j in range(3):
                table[i].append(chr(n))
                n += 1
            if i == 5 or i == 7:
                table[i].append(chr(n))
                n += 1
        
        l = 1
        
        for num in digits:
            l *= len(table[int(num) - 2])
        result = [''] * l
        for num in digits:
            num = int(num) - 2
            c = len(table[num])
            for i in range(l):
                result[i] += table[num][i % c]
            result.sort()
        return result
                
                
        
        