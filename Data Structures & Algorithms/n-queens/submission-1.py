class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col = [False] * n
        posDiag = [False] * (n * 2)
        negDiag = [False] * (n * 2)

        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if col[c] or posDiag[r + c] or negDiag[r - c + n]:
                    continue
                board[r][c] = "Q"
                col[c] = True
                posDiag[r + c] = True
                negDiag[r - c + n] = True

                backTrack(r + 1)
                board[r][c] = "."
                col[c] = False
                posDiag[r + c] = False
                negDiag[r - c + n] = False
        backTrack(0)
        return res
