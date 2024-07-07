class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag = set[int]()
        negDiag = set[int]()
        colSet = set[int]()

        res = 0

        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            for col in range(n):
                if col in colSet or (row + col) in negDiag or (row - col) in posDiag:
                    continue
                colSet.add(col)
                negDiag.add((row + col))
                posDiag.add((row - col))

                backtrack(row + 1)

                colSet.remove(col)
                negDiag.remove((row + col))
                posDiag.remove((row - col))
            return

        backtrack(0)
        return res


if __name__ == '__main__':
    n = 4
    s = Solution()
    a = s.totalNQueens(n)
    print(a)
