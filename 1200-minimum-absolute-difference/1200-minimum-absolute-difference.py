class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()

        diff = float('inf')

        for i in range(len(arr) - 1):
            diff = min(diff, arr[i + 1] - arr[i])

        ans = []

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == diff:
                ans.append([arr[i], arr[i + 1]])

        return ans