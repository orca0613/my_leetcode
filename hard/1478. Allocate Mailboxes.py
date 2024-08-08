# Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

# Return the minimum total distance between each house and its nearest mailbox.

# The test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:


# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
# Example 2:


# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.


from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        total_houses = len(houses)
        memo = {}
        def get_distance(lst):
            l = len(lst)
            mail_box = lst[l // 2]
            r = 0
            for h in lst:
                r += abs(mail_box - h)
            return r
        
        def get_total_distance(idx, n):
            if total_houses - idx <= n:
                return 0
            key = (idx, n)
            r = float("inf")
            if key in memo:
                return memo[key]
            if n == 1:
                r = get_distance(houses[idx:])
                memo[key] = r
                return r

            for i in range(idx, total_houses - n + 1):
                r = min(r, get_distance(houses[idx:i + 1]) + get_total_distance(i + 1, n - 1))
                
            memo[key] = r
            return r
        
        return get_total_distance(0, k)
            
            
        
        
        