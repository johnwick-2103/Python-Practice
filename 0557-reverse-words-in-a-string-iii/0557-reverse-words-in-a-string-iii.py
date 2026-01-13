class Solution:
    def reverseWords(self, s: str) -> str:
         
       # return " ".join(word[::-1] for word in s.split())
 
        words = s.split(" ")
        result = []

        for word in words:
            result.append(word[::-1])

        return " ".join(result)
