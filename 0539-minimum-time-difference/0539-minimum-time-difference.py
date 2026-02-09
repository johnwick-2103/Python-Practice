class Solution:
    def findMinDifference(self, timePoints):
        minutes = []

        for t in timePoints:
            h, m = t.split(":")
            minutes.append(int(h) * 60 + int(m))

        minutes.sort()

        min_diff = 1440 

        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])

        return min_diff
