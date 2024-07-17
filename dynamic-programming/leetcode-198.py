from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            robopt1 = dfs(i + 2) + nums[i]
            robopt2 = dfs(i + 1)
            dp[i] = max(robopt1, robopt2)
            return dp[i]

        return dfs(0)

    def robV2(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    a = s.rob(nums)
    print(a)
