# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

# Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

# Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

# At the stage of rotating the ring to spell the key character key[i]:

# You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
# If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
 

# Example 1:


# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
# For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.
# Example 2:

# Input: ring = "godding", key = "godding"
# Output: 13

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        length = len(ring)
        memo = [[] for _ in range(26)]
        record = {}
        answer = 0
        cur_pos = 0
        
        for i in range(len(ring)):
            k = ring[i]
            memo[ord(k) - 97].append(i)
        
        def clockwise(cur, target):
            for n in memo[target]:
                if n >= cur:
                    return n
            return memo[target][0]
        
        def counter_clockwise(cur, target):
            for i in range(len(memo[target]) - 1, -1, -1):
                n = memo[target][i]
                if n <= cur:
                    return n
            return memo[target][-1]
                
        def get_distance(idx, cur):
            if idx == len(key):
                return 0
            KEY = (idx, cur)
            if KEY in record:
                return record[KEY]
            t = ord(key[idx]) - 97
            right = clockwise(cur, t)
            left = counter_clockwise(cur, t)
            r = min(abs(right - cur), right + length - cur, cur + length - right) + 1
            l = min(abs(left - cur), left + length - cur, cur + length - left) + 1
            record[KEY] = min(r + get_distance(idx + 1, right), l + get_distance(idx + 1, left))
            return record[KEY]
        return get_distance(0, 0)