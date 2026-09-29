class Solution:
    def wordSubsets(self, words1, words2):
        required = [0] * 26

    
        for word in words2:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                required[i] = max(required[i], count[i])

        result = []

    
        for word in words1:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            valid = True

            for i in range(26):
                if count[i] < required[i]:
                    valid = False
                    break

            if valid:
                result.append(word)

        return result