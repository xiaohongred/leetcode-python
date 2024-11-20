class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down memoization
        cache = {}

        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in cache:
                return cache[(i, j)]
            # i could out of bound
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # 如果 p[j+1] 是 *, 需要判断用不用这个*匹配
            if (j + 1) < len(p) and p[j + 1] == '*':
                # ### dont use *
                res = dfs(i, j + 2) or \
                      (match and dfs(i + 1, j))  # use *
                cache[(i, j)] = res
                return res
            # 如果 p[j+1] 不是 *, 则看 s[i]  p[j] 是否匹配
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            else:
                cache[(i, j)] = False
                return False

        return dfs(0, 0)


if __name__ == '__main__':
    solu = Solution()
    s = "aa"
    p = "a"
    a = solu.isMatch(s, p)
    print(a)

    s = "aa"
    p = "a*"
    a = solu.isMatch(s, p)
    print(a)

    s = "ab"
    p = ".*"
    a = solu.isMatch(s, p)
    print(a)
