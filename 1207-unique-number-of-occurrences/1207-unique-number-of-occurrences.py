class Solution:
    def uniqueOccurrences(self, arr):
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        freq = list(count.values())

        return len(freq) == len(set(freq))