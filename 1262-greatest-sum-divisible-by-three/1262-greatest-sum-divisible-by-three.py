class Solution:
    def maxSumDivThree(self, nums):
        dp = [0, 0, 0]

        for num in nums:
            old = dp[:]

            for total in old:
                new_sum = total + num
                remainder = new_sum % 3

                dp[remainder] = max(dp[remainder], new_sum)

        return dp[0]