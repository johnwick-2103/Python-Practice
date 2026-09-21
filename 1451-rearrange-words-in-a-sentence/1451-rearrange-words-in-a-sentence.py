class Solution:
    def arrangeWords(self, text):
        words = text.lower().split()

        words.sort(key=len)

        words[0] = words[0].capitalize()

        return " ".join(words)