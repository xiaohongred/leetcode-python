from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = {}

        def dfs(i):  # 返回值是 从第i天开始到结束旅行，需要的钱
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)

    def mincostTicketsV2(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))
        return dp[0]


if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]

    s = Solution()
    a = s.mincostTickets(days, costs)
    print(a)

    a = s.mincostTicketsV2(days, costs)
    print(a)
