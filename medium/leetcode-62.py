class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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
