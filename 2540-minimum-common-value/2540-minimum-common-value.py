class Solution:
    def getCommon(self, nums1, nums2):
        s = set(nums1)
        
        for num in nums2:
            if num in s:
                return num
        
        return -1