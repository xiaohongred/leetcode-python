from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0, 0]

        for i in range(2, len(cost) + 1):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))

        return dp[len(cost)]

    def minCostClimbingStairsV2(self, cost: List[int]) -> int:

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


if __name__ == '__main__':
    cost = [10, 15, 20]
    s = Solution()
    a = s.minCostClimbingStairs(cost)
    print(a)

    cost2 = [10, 15, 20]
    b = s.minCostClimbingStairsV2(cost2)
    print(b)
