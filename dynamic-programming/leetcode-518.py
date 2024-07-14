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
        # dp 二维数组， amount+1 行， 硬币个数+1 列
        dp[0] = [1] * (len(coins) + 1)  # 第0行， 组成amount=0的方式， 有一种

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]  # skip coins[i]

                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]  # include skip coins[i]
        return dp[amount][0]

    def changeV3(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]

            dp = nextDP
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    a = s.change(amount, coins)
    print(a)

    a = s.changeV2(amount, coins)
    print(a)

    a = s.changeV3(amount, coins)
    print(a)
