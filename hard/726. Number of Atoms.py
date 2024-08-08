# 726. Number of Atoms
# Hard

# 1717

# 361

# Add to List

# Share
# Given a string formula representing a chemical formula, return the count of each atom.

# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.

# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.

# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

# Example 1:

# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# Example 2:

# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:

# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

# Constraints:

# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.

from collections import defaultdict
class Solution:
  def countOfAtoms(self, formula: str) -> str:
    atoms = defaultdict(int)
    storage = [""]
    temp = {}


    
    def decode(s: str):
      d = defaultdict(int)
      cnt = ""
      atom = ""
      for char in s:
        if char.isdigit():
          cnt += char
        elif char.islower():
          atom += char
        else:
          if not atom:
            atom = char
            continue
          n = int(cnt) if cnt else 1
          d[atom] += n
          atom = char
          cnt = ""
      n = int(cnt) if cnt else 1
      d[atom] += n
      return d
    

    def encode(d):
      s = ""
      for atom in d.keys():
        s += atom + str(d[atom])
      return s
    

    def multiply(d, n):
      for atom in d.keys():
        d[atom] *= n
      return d

    i = 0
    while i < len(formula):
      char = formula[i]
      if char == "(":
        storage.append([""])
      elif char == ")":
        temp = decode(storage.pop())
        n = ""
        while i < len(formula) - 1 and formula[i + 1].isdigit():
          i += 1
          n += formula[i]
        n = int(n) if n else 1
        temp = multiply(temp, n)
        storage[-1] += encode(temp)
        temp = {}
      else:
        storage[-1] += char
      i += 1
    
    result = decode(storage.pop())
    answer = ""
    sorted_key = sorted(list(result.keys()))
    for key in sorted_key:
      answer += key
      answer += str(result[key]) if result[key] > 1 else ""

    return answer