class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        first = s[:k]
        rest = s[k:]
        return first[::-1] + rest