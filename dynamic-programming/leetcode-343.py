class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dfs(num):
            if num == 1:
                return 1
            if num in cache:
                return cache[num]

            res = 0 if num == n else num  # 保证 原始的 n 会被拆散, 其他的数(非n) 可以不拆, 如果没有这个条件，所有的结果都是1
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            cache[num] = res
            return res

        return dfs(n)

    def integerBreakV2(self, n: int) -> int:
        cache = {1: 1}

        def dfs(num):
            if num in cache:
                return cache[num]

            res = 0 if num == n else num  # 保证 原始的 n 会被拆散, 其他的数(非n) 可以不拆, 如果没有这个条件，所有的结果都是1
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            cache[num] = res
            return res

        return dfs(n)

    def integerBreakDP(self, n: int) -> int:
        dp = {1: 1}
        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num  # n 必须被拆分 由n分解后得到的数num，可以保持为num

            # 这里计算出 dp[num] 的值  也就是说 num 被拆分后(如果 num 不是 n,可以不被拆分)，乘积最大能是 dp[num]
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        
        return dp[n]


if __name__ == '__main__':
    n = 2
    s = Solution()
    a = s.integerBreak(n)
    print(a)

    n = 5
    a = s.integerBreak(n)
    print(a)

    n = 10
    a = s.integerBreak(n)
    print(a)

    n = 2
    a = s.integerBreakDP(n)
    print(a)

    n = 5
    a = s.integerBreakDP(n)
    print(a)

    n = 10
    a = s.integerBreakDP(n)
    print(a)
