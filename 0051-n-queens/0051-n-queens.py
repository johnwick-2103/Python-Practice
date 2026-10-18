class Solution:
    def solveNQueens(self, n):
        result = []
        board = ["." * n for _ in range(n)]

        def backtrack(row, cols, d1, d2):
            if row == n:
                result.append(board[:])
                return

            for col in range(n):
                if col in cols or row - col in d1 or row + col in d2:
                    continue

                cols.add(col)
                d1.add(row - col)
                d2.add(row + col)

                board[row] = "." * col + "Q" + "." * (n - col - 1)
                backtrack(row + 1, cols, d1, d2)

                cols.remove(col)
                d1.remove(row - col)
                d2.remove(row + col)

        backtrack(0, set(), set(), set())
        return result