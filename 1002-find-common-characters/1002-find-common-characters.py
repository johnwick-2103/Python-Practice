class Solution:
    def commonChars(self, words):
        result = []
        common = {}
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1
        for word in words[1:]:
            temp = {}
            for ch in word:
                temp[ch] = temp.get(ch, 0) + 1
            for ch in common:
                common[ch] = min(common[ch], temp.get(ch, 0))
        for ch in common:
            for _ in range(common[ch]):
                result.append(ch)

        return result
