from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # dp[amount] 保存的是要组成 amount 最好需要多少硬币
        dp[0] = 0

        for amountNum in range(1, amount + 1):
            for c in coins:
                if amountNum - c >= 0:
                    dp[amountNum] = min(dp[amountNum], 1 + dp[amountNum - c])  # 比较 不要当前硬币 和要当前硬币， 哪种方案需要的硬币更少

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coinChangeV2(self, coins: List[int], amount: int) -> int:
        cache = {}
        coins.sort()

        def dfs(amount: int) -> int:
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            min_coins = float("inf")
            for c in coins:
                if amount - c >= 0:
                    sub = dfs(amount - c)
                    if sub != -1:
                        min_coins = min(min_coins, 1 + sub)
                else:
                    break
            cache[amount] = min_coins if min_coins != float('inf') else -1
            return cache[amount]

        res = dfs(amount)
        return res


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    s = Solution()
    a = s.coinChange(coins, amount)
    print(a)

    a = s.coinChangeV2(coins, amount)
    print(a)
