class Solution:
    def intersection(self, nums1, nums2):
        result = []
        set1 = set(nums1)

        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)

        return result
