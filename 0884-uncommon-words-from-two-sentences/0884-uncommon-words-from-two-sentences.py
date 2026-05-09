class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        words = (s1 + " " + s2).split()
        ans = []

        for w in words:
            if words.count(w) == 1:
                ans.append(w)

        return ans