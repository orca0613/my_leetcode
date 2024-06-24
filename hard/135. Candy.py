# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        ratings.append(10 ** 5)
        r = [1] * (l + 1)
        for i in range(l):
            c = ratings[i]
            if c <= ratings[i - 1] and c <= ratings[i + 1]:
                idx = i - 1
                while idx >= 0 and ratings[idx] > c:
                    r[idx] = max(r[idx + 1] + 1, r[idx])
                    c = ratings[idx]
                    idx -= 1
                c = ratings[i]
                idx = i + 1
                while idx < l and ratings[idx] > c:
                    r[idx] = max(r[idx - 1] + 1, r[idx])
                    c = ratings[idx]
                    idx += 1
        return sum(r[:-1])
                    
                    
        