# You are given two integer arrays nums1 and nums2 of length n.

# The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).

# For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
# Rearrange the elements of nums2 such that the resulting XOR sum is minimized.

# Return the XOR sum after the rearrangement.

 

# Example 1:

# Input: nums1 = [1,2], nums2 = [2,3]
# Output: 2
# Explanation: Rearrange nums2 so that it becomes [3,2].
# The XOR sum is (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2.
# Example 2:

# Input: nums1 = [1,0,3], nums2 = [5,3,4]
# Output: 8
# Explanation: Rearrange nums2 so that it becomes [5,4,3]. 
# The XOR sum is (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8.

class Solution:
    def minimumXORSum(self, nums1, nums2) -> int:
        
        n = len(nums1)
        memo = {}
        
        def toggle(idx, cur):
            if idx == n:
                return 0
            if cur in memo:
                return memo[cur]
            r = float("inf")
            num = nums1[idx]
            for i in range(n):
                shifted = 1 << i
                x = num ^ nums2[i]
                if not cur & shifted:
                    r = min(r, x + toggle(idx + 1, cur + shifted))
            memo[cur] = r
            return r
        
        return toggle(0, 0)
                    
                
        