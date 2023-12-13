from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amountNum in range(1, amount + 1):
            for c in coins:
                if amountNum - c >= 0:
                    dp[amountNum] = min(dp[amountNum], 1 + dp[amountNum - c])

        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    s = Solution()
    a = s.coinChange(coins, amount)
    print(a)
