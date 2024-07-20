from typing import List


class Solution:
    def rob_1(self, nums: List[int]) -> int:
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

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:-1]))


if __name__ == '__main__':
    nums = [2, 3, 2]
    s = Solution()

    a = s.rob(nums)
    print(a)
