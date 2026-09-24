class Solution:
    def addedInteger(self, nums1, nums2):
        n = len(nums1)
        x = (sum(nums2) - sum(nums1)) // n
        return x