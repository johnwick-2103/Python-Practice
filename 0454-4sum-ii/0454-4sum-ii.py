from collections import Counter

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        countAB = Counter()
        
        # All sums of nums1 and nums2
        for a in nums1:
            for b in nums2:
                countAB[a + b] += 1
        
        result = 0
        
        # Match with nums3 and nums4
        for c in nums3:
            for d in nums4:
                result += countAB[-(c + d)]
        
        return result
