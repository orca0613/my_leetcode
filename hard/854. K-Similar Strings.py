# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

# Example 1:

# Input: s1 = "ab", s2 = "ba"
# Output: 1
# Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
# Example 2:

# Input: s1 = "abc", s2 = "bca"
# Output: 2
# Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:

        memo = {}
        
        def match(word):
            if not word:
                return 0
            if word in memo:
                return memo[word]
            l = len(word)
            if word[0] == s2[-l]:
                return match(word[1:])
            r = 100
            for i in range(1, l):
                if word[i] == s2[-l]:
                    r = min(r, 1 + match(word[1:i] + word[0] + word[i + 1:]))
            memo[word] = r
            return r
        return match(s1)
            
                
        