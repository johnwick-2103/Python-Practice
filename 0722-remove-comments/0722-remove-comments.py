class Solution:
    def removeComments(self, source):
        result = []
        block = False
        current = ""

        for line in source:
            i = 0

            while i < len(line):
             
                if not block and i + 1 < len(line) and line[i:i + 2] == "/*":
                    block = True
                    i += 2

                elif block and i + 1 < len(line) and line[i:i + 2] == "*/":
                    block = False
                    i += 2

                elif not block and i + 1 < len(line) and line[i:i + 2] == "//":
                    break

                else:
                    if not block:
                        current += line[i]
                    i += 1

            if not block and current:
                result.append(current)
                current = ""

        return result