class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                s1 = s[i + 1 : n - i]
                s2 = s[i : n - i - 1]
                return s1 == s1[::-1] or s2 == s2[::-1]

        return True
