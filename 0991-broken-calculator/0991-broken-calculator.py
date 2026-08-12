class Solution:
    def brokenCalc(self, startValue, target):
        count = 0

        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

            count += 1

        return count + (startValue - target)