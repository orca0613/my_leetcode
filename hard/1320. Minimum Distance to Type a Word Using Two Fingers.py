
# You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

# For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# Given the string word, return the minimum total distance to type such string using only two fingers.

# The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

# Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

# Example 1:

# Input: word = "CAKE"
# Output: 3
# Explanation: Using two fingers, one optimal way to type "CAKE" is: 
# Finger 1 on letter 'C' -> cost = 0 
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
# Finger 2 on letter 'K' -> cost = 0 
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
# Total distance = 3
# Example 2:

# Input: word = "HAPPY"
# Output: 6
# Explanation: Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def get_distance(s1, s2):
            n1, n2 = ord(s1) - 65, ord(s2) - 65
            y1, x1 = n1 // 6, n1 % 6
            y2, x2 = n2 // 6, n2 % 6
            return abs(y1 - y2) + abs(x1 - x2)
        
        cache = {}
        l = len(word)
        result = float("inf")
        
        def tipe(left, right, idx):
            if idx == l:
                return 0
            if right < left:
                left, right = right, left
            key = (left, right, idx)
            if key in cache:
                return cache[key]
            r = float("inf")
            target = word[idx]
            r = min(r, get_distance(left, target) + tipe(target, right, idx + 1))
            r = min(r, get_distance(right, target) + tipe(left, target, idx + 1))
            
            cache[key] = r
            return r
        
        for i in range(65, 91):
            for j in range(i + 1, 91):
                result = min(result, tipe(chr(i), chr(j), 0))
                
        return result
        