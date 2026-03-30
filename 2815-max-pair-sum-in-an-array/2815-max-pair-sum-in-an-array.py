class Solution:
    def maxSum(self, nums):
        
        def largest_digit(num):
            return max(int(d) for d in str(num))
        
        groups = {}
        
        for num in nums:
            d = largest_digit(num)
            if d not in groups:
                groups[d] = []
            groups[d].append(num)
        
        max_sum = -1
        
        for values in groups.values():
            if len(values) >= 2:
                values.sort(reverse=True)
                max_sum = max(max_sum, values[0] + values[1])
        
        return max_sum