class Solution:
    def buildArray(self, target, n):
        result = []
        target_index = 0
        
        for num in range(1, n + 1):
            if target_index >= len(target):
                break
            
            result.append("Push")
            
            if num == target[target_index]:
                target_index += 1
            else:
                result.append("Pop")
        
        return result
