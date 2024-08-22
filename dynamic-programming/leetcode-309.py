from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Sell
        # if Buy -> i+1
        # if Sell -> i + 2
        dp = {}  # key=(i, buying) val = max_profile

        def dfs(i, buying):
            # i 第 i 天， buying -> 第i天的行为 是否买入,
            # 返回: 第i天做buying操作能够获得的最大收益

            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:  # 买入或者不操作
                buy = dfs(i + 1, not buying) - prices[i]  # 第i天买入，花费了 prices[i] 元
                cooldown = dfs(i + 1, buying)  # 第 i 天不买入，选择到 i+1 天再去定买入还是不买入
                dp[(i, buying)] = max(buy, cooldown)
            else:  # 卖出或者不操作
                sell = dfs(i + 2, not buying) + prices[i]  # 第i天卖出，获取 prices[i] 元, i+2 天才能再次买入
                cooldown = dfs(i + 1, buying)  # 第 i 天不卖出，可以选择在 i+1 天卖出或者不卖出
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    s = Solution()
    a = s.maxProfit(prices)
    print(a)
