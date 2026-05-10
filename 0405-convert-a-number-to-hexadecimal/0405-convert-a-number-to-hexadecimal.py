class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        ans = ""

        num &= 0xffffffff

        while num:
            ans = hex_chars[num % 16] + ans
            num //= 16

        return ans