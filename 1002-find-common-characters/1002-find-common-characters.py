from collections import Counter
class Solution:
    def commonChars(self, words):
        res = Counter(words[0])
        for w in words[1:]:
            res &= Counter(w)
        return list(res.elements())
