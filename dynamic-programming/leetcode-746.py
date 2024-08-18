from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}  # 从第i个台阶开始爬，需要支付的最小费用

        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            res = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
            dp[i] = res
            return res

        return min(dfs(0), dfs(1))

    def minCostClimbingStairsDP(self, cost: List[int]) -> int:
        dp = {len(cost) - 1: cost[-1], len(cost): 0}
        for i in range(len(cost) - 2, -1, -1):
            res = float("inf")
            if i + 1 >= len(cost) or i + 2 >= len(cost):
                res = cost[i]
            res = min(res, cost[i] + dp[i + 1], cost[i] + dp[i + 2])
            dp[i] = res
        return min(dp[0], dp[1])

    def minCostClimbingStairsDP_V2(self, cost: List[int]) -> int:
        # [10, 15, 20] 0
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        return min(cost[0], cost[1])


if __name__ == '__main__':
    cost = [10, 15, 20]
    s = Solution()
    a = s.minCostClimbingStairs(cost)
    print(a)

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    a = s.minCostClimbingStairs(cost)
    print(a)

    cost = [10, 15, 20]
    a = s.minCostClimbingStairsDP(cost)
    print(a)

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    a = s.minCostClimbingStairsDP(cost)
    print(a)
