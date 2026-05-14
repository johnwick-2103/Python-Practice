class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = ""

        for c in s:
            if res and res[-1] == c:
                res = res[:-1]
            else:
                res += c

        return res