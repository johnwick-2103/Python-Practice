class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [""] * len(words)

        for w in words:
            pos = int(w[-1]) - 1
            res[pos] = w[:-1]

        return " ".join(res)