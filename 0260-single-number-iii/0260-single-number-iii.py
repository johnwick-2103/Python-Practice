class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n

        diff_bit = xor & -xor

        a = b = 0
        for n in nums:
            if n & diff_bit:
                a ^= n
            else:
                b ^= n

        return [a, b]
