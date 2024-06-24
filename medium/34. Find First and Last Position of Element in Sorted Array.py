class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        def searching(s, e, n):
            if s >= e:
                if nums[s] != n:
                    return -1
                return s
            mid = (s + e) // 2
            if nums[mid] > n:
                return searching(s, mid - 1, n)
            if nums[mid] < n:
                return searching(mid + 1, e, n)
            return mid
        
        r =  searching(0, len(nums) - 1, target)
        if r < 0:
            return[-1, -1]
        else:
            s, e = r, r
            while s >= 0 and nums[s] == target:
                s -= 1
            while e < len(nums) and nums[e] == target:
                e += 1
            return [s + 1, e - 1]
                
            
            
            