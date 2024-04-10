from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)

    def changeV2(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):  # a amount 行
            for i in range(len(coins) - 1, -1, -1):  # i 第i个硬币，面值为coins[i]
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

    def changeV3(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1
            for a in range(1, amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a - coins[i]]
            dp = nextDp
        return dp[amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    s = Solution()
    a = s.changeV3(amount, coins)
    print(a)

    a = s.changeV2(amount, coins)
    print(a)
