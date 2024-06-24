# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        table =[]
        answer = []
        l = len(s)
        
        for i in range(l):
            table.append([])
            for j in range(i + 1, l + 1):
                table[i].append(s[i:j])
                
        w_dict = set(wordDict)
        
        def w_break(idx, word):
            if idx == l:
                answer.append(word[:-1])
                return
            
            for piece in table[idx]:
                if piece in w_dict:
                    w_break(idx + len(piece), word + piece + " ")
            
        
        w_break(0, "")
        return answer
                
        