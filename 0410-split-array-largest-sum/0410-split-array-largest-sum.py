class Solution:
    def splitArray(self, nums, k): 
        def canSplit(maxSum):
            current_sum = 0
            pieces = 1  
            
            for num in nums:
                if current_sum + num > maxSum:
                    pieces += 1
                    current_sum = num
                else:
                    current_sum += num
            
            return pieces <= k
        
        low = max(nums)
        high = sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
