from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != (amount + 1) else -1

    def coinChangeDFS(self, coins: List[int], amount: int) -> int:
        cache = {}
        coins.sort()

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]

            min_coins = float('inf')
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

    def coinChangeDFSV2(self, coins: List[int], amount: int) -> int:
        cache = {}
        coins.sort()

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]

            min_coins = amount + 1
            for c in coins:
                if amount - c >= 0:
                    sub = dfs(amount - c)
                    if sub != -1:
                        min_coins = min(min_coins, 1 + sub)
                else:
                    break

            cache[amount] = min_coins if min_coins != (amount + 1) else -1
            return cache[amount]

        res = dfs(amount)
        return res


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    s = Solution()
    a = s.coinChange(coins, amount)
    print(a)

    coins = [2]
    amount = 3
    a = s.coinChange(coins, amount)
    print(a)

    coins = [1, 2, 5]
    amount = 11
    a = s.coinChangeDFSV2(coins, amount)
    print(a)

    coins = [2]
    amount = 3
    a = s.coinChangeDFSV2(coins, amount)
    print(a)
