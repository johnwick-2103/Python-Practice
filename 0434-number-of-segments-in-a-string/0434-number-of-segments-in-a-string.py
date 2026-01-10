class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        inWord = False

        for ch in s:
            if ch != ' ' and not inWord:
                count += 1
                inWord = True
            elif ch == ' ':
                inWord = False

        return count
