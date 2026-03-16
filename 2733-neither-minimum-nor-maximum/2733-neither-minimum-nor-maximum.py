class Solution:
    def findNonMinOrMax(self, nums):
        mn = min(nums)
        mx = max(nums)
        
        for num in nums:
            if num != mn and num != mx:
                return num
        
        return -1