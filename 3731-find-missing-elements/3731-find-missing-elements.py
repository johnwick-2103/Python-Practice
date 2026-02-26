class Solution:
    def findMissingElements(self, nums):
        smallest = min(nums)
        largest = max(nums)
        
        num_set = set(nums)
        missing = []
        
        for num in range(smallest, largest + 1):
            if num not in num_set:
                missing.append(num)
        
        return missing