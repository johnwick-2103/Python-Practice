class Solution:
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        
        for i in range(32):
            count1 = 0
            
            for num in nums:
                if (num >> i) & 1:
                    count1 += 1
            
            count0 = n - count1
            total += count1 * count0
        
        return total
