class Solution:
    def beautifulArray(self, n):
        result = [1]
        
        while len(result) < n:
            temp = []
        
            for x in result:
                if 2 * x - 1 <= n:
                    temp.append(2 * x - 1)
          
            for x in result:
                if 2 * x <= n:
                    temp.append(2 * x)
            
            result = temp
        
        return result
