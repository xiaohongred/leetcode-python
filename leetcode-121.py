from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1  # left = buy, right=sell
        while r < len(prices):
            if prices[l] < prices[r]:
                profile = prices[r] - prices[l]
                maxP = max(maxP, profile)
            else:
                l = r

            r += 1

        return maxP



if __name__ == '__main__':
    s = Solution()

    nums = [7,1,5,3,6,4]
    a = s.maxProfit(nums)
    print(a)