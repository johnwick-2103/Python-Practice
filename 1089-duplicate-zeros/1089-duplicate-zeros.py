class Solution:
    def duplicateZeros(self, arr):
        result = []
        
        for num in arr:
            if num == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(num)
        
        for i in range(len(arr)):
            arr[i] = result[i]