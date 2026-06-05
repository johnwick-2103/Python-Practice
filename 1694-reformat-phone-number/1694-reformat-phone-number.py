class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")

        ans = []

        while len(number) > 4:
            ans.append(number[:3])
            number = number[3:]

        if len(number) == 4:
            ans.append(number[:2])
            ans.append(number[2:])
        else:
            ans.append(number)

        return "-".join(ans)