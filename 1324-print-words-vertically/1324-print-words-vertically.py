class Solution:
    def printVertically(self, s):
        words = s.split()

        ans = []
        max_len = max(len(word) for word in words)

        for i in range(max_len):
            temp = ""

            for word in words:
                if i < len(word):
                    temp += word[i]
                else:
                    temp += " "

            ans.append(temp.rstrip())

        return ans