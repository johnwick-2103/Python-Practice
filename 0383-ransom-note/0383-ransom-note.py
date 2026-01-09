class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        
        for ch in ransomNote:
            if ch not in mag:
                return False
            mag.remove(ch)
        return True
