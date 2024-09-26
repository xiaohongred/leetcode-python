from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        miniStock = prices[0]
        for price in prices:
            curProfit = price - miniStock
            profit = max(profit, curProfit)

            miniStock = min(price, miniStock)
        return profit

    def maxProfitV2(self, prices: List[int]) -> int:
        l, r = 0, 1  # left = buy , right = sell
        maxP = 0
        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    a = s.maxProfit(prices)
    print(a)

    prices = [7, 6, 4, 3, 1]
    a = s.maxProfit(prices)
    print(a)

    prices = [7, 1, 5, 3, 6, 4]
    a = s.maxProfitV2(prices)
    print(a)

    prices = [7, 6, 4, 3, 1]
    a = s.maxProfitV2(prices)
    print(a)
