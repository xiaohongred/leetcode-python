import locale


class Solution:
    def minDays(self, n: int) -> int:
        dayMaps = {}

        def dfs(orgNum: int) -> int:
            if orgNum == 0:
                return 0
            if orgNum == 1:
                return 1
            if orgNum in dayMaps:
                return dayMaps[orgNum]

            typeDay1 = orgNum
            typeDay2 = orgNum
            if orgNum % 2 == 0:
                typeDay1 = 1 + dfs(orgNum / 2)

            if orgNum % 3 == 0:
                typeDay2 = 1 + dfs(orgNum / 3)

            typeDay0 = 1 + dfs(orgNum - 1)
            res = min(typeDay0, typeDay1, typeDay2)
            dayMaps[orgNum] = res
            return res

        a = dfs(n)

        return int(min(n, a))

    def minDaysV2(self, n: int) -> int:
        if n < 3:
            return n
        if n == 3:
            return 2
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 2
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 2])
            if i % 3 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 3])
            dp[i] = min(dp[i], 1 + dp[i - 1])
        return dp[n]

    def minDaysV3(self, n: int) -> int:
        dp = {0: 0, 1: 1}

        def dfs(n: int) -> int:
            if n in dp:
                return dp[n]
            typeDay1 = dfs(n // 2) + n % 2 + 1
            typeDay2 = dfs(n // 3) + n % 3 + 1
            dp[n] = min(typeDay1, typeDay2)
            return dp[n]

        a = dfs(n)

        return int(min(n, a))


if __name__ == '__main__':
    n = 10
    s = Solution()
    a = s.minDays(n)
    print(a)

    # n = 5126970
    # s = Solution()
    # a = s.minDaysV2(n)
    # print(a)

    n = 5126970
    s = Solution()
    a = s.minDaysV3(n)
    print(a)
