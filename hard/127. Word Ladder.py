# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def similar(w1, w2):
            n = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    n += 1
                    if n > 1:
                        return False
            return True
        
        memo = {}
        n = 1
        stack = [beginWord]
        t = [beginWord]
        while t:
            n += 1
            t = []
            while stack:
                word = stack.pop()
                for i in range(len(wordList) - 1, -1, -1):
                    if similar(word, wordList[i]):
                        t.append(wordList.pop(i))
            if endWord in t:
                return n
            stack = t
        return 0
            