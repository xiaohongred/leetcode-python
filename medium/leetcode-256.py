# https://www.lintcode.com/problem/515/
from typing import (
    List,
)


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        # costs[i][j] i is house, j is color
        n = len(costs)
        m = len(costs[0])
        dp = [0, 0, 0]
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]

        return min(dp)


if __name__ == '__main__':
    costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    s = Solution()
    a = s.min_cost(costs)
    print(a)
