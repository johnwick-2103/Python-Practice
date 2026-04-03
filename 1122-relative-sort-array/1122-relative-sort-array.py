from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        result = []
        
        for num in arr2:
            result.extend([num] * count[num])
            count.pop(num)
        
        remaining = []
        for num in count:
            remaining.extend([num] * count[num])
        
        result.extend(sorted(remaining))
        
        return result