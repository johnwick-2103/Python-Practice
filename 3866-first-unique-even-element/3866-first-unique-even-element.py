from collections import Counter

class Solution:
    def firstUniqueEven(self, nums):
        count = Counter(nums)
        
        for num in nums:
            if num % 2 == 0 and count[num] == 1:
                return num
        
        return -1