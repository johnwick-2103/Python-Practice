class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in memo:
                return memo[(i, total)]

            count = (
                backtrack(i + 1, total + nums[i]) +
                backtrack(i + 1, total - nums[i])
            )

            memo[(i, total)] = count
            return count

        return backtrack(0, 0)
