class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for n in nums:
            xor_all ^= n

        diff_bit = xor_all & -xor_all

        a = b = 0
        for n in nums:
            if n & diff_bit:
                a ^= n
            else:
                b ^= n

        return [a, b]
