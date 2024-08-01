class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == "" and t == "":
            return 1
        if s == "" and t != "":
            return 0
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"

    solu = Solution()
    a = solu.numDistinct(s, t)
    print(a)

    s = "babgbag"
    t = "bag"
    a = solu.numDistinct(s, t)
    print(a)
