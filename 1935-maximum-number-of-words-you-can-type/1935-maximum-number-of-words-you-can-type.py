class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0

        for word in words:
            ok = True

            for ch in word:
                if ch in brokenLetters:
                    ok = False
                    break

            if ok:
                count += 1

        return count