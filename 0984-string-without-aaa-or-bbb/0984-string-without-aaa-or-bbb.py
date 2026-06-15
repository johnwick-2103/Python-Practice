class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""

        while a > 0 or b > 0:

            if a > b:
                if a > 0:
                    res += "a"
                    a -= 1
                if a > b and a > 0:
                    res += "a"
                    a -= 1
                if b > 0:
                    res += "b"
                    b -= 1

            else:
                if b > 0:
                    res += "b"
                    b -= 1
                if b > a and b > 0:
                    res += "b"
                    b -= 1
                if a > 0:
                    res += "a"
                    a -= 1

        return res