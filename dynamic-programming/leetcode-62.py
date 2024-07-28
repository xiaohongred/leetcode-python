class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        for i in range(m):
            cache[i][0] = 1
        for i in range(n):
            cache[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
        return cache[m - 1][n - 1]

    def uniquePathsV2(self, m: int, n: int):
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


if __name__ == '__main__':
    m = 3
    n = 7

    s = Solution()
    a = s.uniquePaths(m, n)
    print(a)
