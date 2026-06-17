class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        lower = upper = digit = 1

        for c in password:
            if c.islower():
                lower = 0
            elif c.isupper():
                upper = 0
            elif c.isdigit():
                digit = 0

        missing = lower + upper + digit

        replace = 0
        one = two = 0

        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2

                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1

                replace += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        replace -= min(delete, one)
        delete -= min(delete, one)

        use = min(delete // 2, two)
        replace -= use
        delete -= use * 2

        replace -= delete // 3

        return (n - 20) + max(missing, replace)