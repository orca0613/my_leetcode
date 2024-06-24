# You are given an array nums of positive integers and a positive integer k.

# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

# Return the number of non-empty beautiful subsets of the array nums.

# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

# Example 1:

# Input: nums = [2,4,6], k = 2
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
# It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
# Example 2:

# Input: nums = [1], k = 1
# Output: 1
# Explanation: The beautiful subset of the array nums is [1].
# It can be proved that there is only 1 beautiful subset in the array [1].

class Solution:
    def beautifulSubsets(self, nums, k: int) -> int:
        
        nums.sort()
        ban = []
        l = len(nums)
        answer = 0
        
        for i in range(l):
            for j in range(i + 1, l):
                if nums[j] - nums[i] == k:
                    n = (1 << i) + (1 << j)
                    ban.append(n)
        
        def get_beauty(num, idx):
            if idx == l:
                return 1
            r = 1
            for i in range(idx, l):
                n = num + (1 << i)
                x = True
                for b in ban:
                    if (n & b) == b:
                        x = False
                        break
                if x:
                    r += get_beauty(n, i + 1)
            return r
        
        for i in range(l):
            answer += get_beauty(1 << i, i + 1)
            
        return answer
        
                    
                    
        