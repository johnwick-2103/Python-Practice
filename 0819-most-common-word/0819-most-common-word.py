from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)
        
        count = Counter(w for w in words if w not in banned_set)
        
        return count.most_common(1)[0][0]
