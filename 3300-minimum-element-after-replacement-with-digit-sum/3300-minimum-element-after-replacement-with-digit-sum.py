class Solution:
    def minElement(self, nums):
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        min_val = float('inf')
        
        for num in nums:
            s = digit_sum(num)
            min_val = min(min_val, s)
        
        return min_val