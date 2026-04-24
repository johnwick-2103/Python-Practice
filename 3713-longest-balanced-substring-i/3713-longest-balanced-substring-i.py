class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            count = {}
            
            for j in range(i, n):
                ch = s[j]
                count[ch] = count.get(ch, 0) + 1
                
                values = list(count.values())
                if len(set(values)) == 1:
                    max_len = max(max_len, j - i + 1)
        
        return max_len