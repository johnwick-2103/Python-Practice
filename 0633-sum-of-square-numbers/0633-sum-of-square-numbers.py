class Solution:
    def judgeSquareSum(self, c):
        a = 0

        while a * a <= c:
            b = int((c - a * a) ** 0.5)

            if b * b == c - a * a:
                return True

            a += 1

        return False