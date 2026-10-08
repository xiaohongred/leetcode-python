from typing import List
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        col = [0] * n
        def valid(r, c):
            for R in range(r):
                C = col[R]
                if r+c == R+C or r-c == R-C:
                    return False
            return True
        def dfs(r, s):  # r表示当前枚举的行号， s表示剩余可以枚举的列号
            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col])  # 第 c 列放皇后  col[i] 代表第i行的皇后在第 col[i] 列
            
            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r+1,s-{c})


        dfs(0, set(range(n)))
        return ans
    def solveNQueensAll(self, n: int) -> list[list[str]]:
        ans = []
        col = [0] * n

        def dfs(r, s):  # r表示当前枚举的行号， s表示剩余可以枚举的列号
            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col])  # 第 c 列放皇后  col[i] 代表第i行的皇后在第 col[i] 列
            
            for c in s:
                if all(r + c != R + col[R] and r - c != R - col[R] for R in range(r)):
                    col[r] = c
                    dfs(r+1,s-{c})


        dfs(0, set(range(n)))
        return ans
    def solveNQueensV3(self, n: int) -> list[list[str]]:
        ans = []
        col = [0] * n
        on_path = [False] * n
        m = 2*n - 1
        diag1 = [False] * m
        diag2 = [False] * m
        def dfs(r):  # r表示当前枚举的行号
            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col])  # 第 c 列放皇后  col[i] 代表第i行的皇后在第 col[i] 列
            
            for c in range(n):
                if not on_path[c] and not diag1[r+c] and not diag2[r-c]:
                    col[r] = c
                    on_path[c] = diag1[r+c] = diag2[r-c] = True
                    dfs(r+1)
                    on_path[c] = diag1[r+c] = diag2[r-c] = False


        dfs(0)
        return ans
    def solveNQueenV2(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        queens = [-1] * n  # queens[row] = col

        def backtrack(row: int) -> None:
            if row == n:
                board = []
                for c in queens:
                    board.append('.' * c + 'Q' + '.' * (n - c - 1))
                res.append(board)
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens[row] = col
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))