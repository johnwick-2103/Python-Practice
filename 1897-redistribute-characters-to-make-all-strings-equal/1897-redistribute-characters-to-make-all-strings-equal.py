class Solution:
    def makeEqual(self, words) -> bool:
        s = "".join(words)

        for ch in set(s):
            if s.count(ch) % len(words):
                return False

        return True