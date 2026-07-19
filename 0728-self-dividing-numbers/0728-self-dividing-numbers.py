class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []

        for num in range(left, right + 1):
            x = num
            while x:
                digit = x % 10

                if digit == 0 or num % digit != 0:
                    break

                x //= 10
            else:
                ans.append(num)

        return ans