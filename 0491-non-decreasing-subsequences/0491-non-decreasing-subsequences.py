class Solution:
    def findSubsequences(self, nums):
        result = []

        def backtrack(start, path):
            if len(path) >= 2:
                result.append(path[:])

            used = set()

            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue

                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])
                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return result