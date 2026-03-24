class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {line: i for i, line in enumerate(valid_lines)}
        
        result = []
        
        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            active = isActive[i]
            
            if not c:
                continue
            if not all(ch.isalnum() or ch == '_' for ch in c):
                continue
            if b not in order:
                continue
            if not active:
                continue
            
            result.append((b, c))

        result.sort(key=lambda x: (order[x[0]], x[1]))
        
        return [c for _, c in result]