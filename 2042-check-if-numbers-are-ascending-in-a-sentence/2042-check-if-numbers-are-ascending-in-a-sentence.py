class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0

        for word in s.split():
            if word.isdigit():
                if int(word) <= prev:
                    return False
                prev = int(word)

        return True