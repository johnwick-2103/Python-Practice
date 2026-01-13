class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # All uppercase
        if word == word.upper():
            return True

        # All lowercase
        if word == word.lower():
            return True

        # First letter uppercase, rest lowercase
        if word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return True

        return False
