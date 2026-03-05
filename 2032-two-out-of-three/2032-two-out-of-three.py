class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        
        result = set()
        
        for num in set1:
            if num in set2 or num in set3:
                result.add(num)
        
        for num in set2:
            if num in set3:
                result.add(num)
        
        return list(result)