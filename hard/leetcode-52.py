class Solution:
    def totalNQueens(self, n: int) -> int:

        # 记录当前皇后影响的行列
        posDiag = set[int]()  # (r + c)
        negDiag = set[int]()  # (r - c)
        colSet = set[int]()

        res = 0

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return
            for c in range(n):  # 迭代遍历每列
                if c in colSet \
                        or (r + c) in posDiag \
                        or (r - c) in negDiag:
                    continue

                # 相当于在 (r, c) 位置放置一个皇后
                colSet.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)  # 递归迭代每行

                # 去掉 (r, c) 位置的皇后
                colSet.remove(c)  # 回溯,恢复状态
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res


if __name__ == '__main__':
    s = Solution()

    n = 4
    a = s.totalNQueens(n)
    print(a)

    n = 1
    a = s.totalNQueens(n)
    print(a)
