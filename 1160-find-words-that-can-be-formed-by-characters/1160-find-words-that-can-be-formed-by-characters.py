from collections import Counter

class Solution:
    def countCharacters(self, words, chars):
        char_count = Counter(chars)
        ans = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= char_count[c] for c in word):
                ans += len(word)

        return ans