class Solution:
    def longestPalindrome(self, s: str) -> int:
        st = set()
        ans = 0

        for ch in s:
            if ch in st:
                ans += 2
                st.remove(ch)
            else:
                st.add(ch)

        if st:
            ans += 1

        return ans