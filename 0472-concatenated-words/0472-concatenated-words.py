class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        result = []
        memo = {}

        def canForm(word):
            if word in memo:
                return memo[word]

            for i in range(1, len(word)):
                left = word[:i]
                right = word[i:]
                if left in word_set and (right in word_set or canForm(right)):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        for word in words:
            word_set.remove(word)       
            if canForm(word):
                result.append(word)
            word_set.add(word)

        return result
