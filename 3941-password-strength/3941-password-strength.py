class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0

        for ch in set(password):

            if ch.islower():
                strength += 1

            elif ch.isupper():
                strength += 2

            elif ch.isdigit():
                strength += 3

            elif ch in "!@#$":
                strength += 5

        return strength