class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)

        letters.reverse()
        special.reverse()

        ans = []
        i = j = 0

        for ch in s:
            if ch.isalpha():
                ans.append(letters[i])
                i += 1
            else:
                ans.append(special[j])
                j += 1

        return "".join(ans)