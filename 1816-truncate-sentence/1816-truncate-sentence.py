class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        ans = []

        for i in range(k):
            ans.append(words[i])

        return " ".join(ans)