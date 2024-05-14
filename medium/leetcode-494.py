from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]

        def dfs(i, curSum):
            if i == len(nums):
                if curSum == target:
                    res[0] = res[0] + 1
                    return
            if i >= len(nums):
                return
            dfs(i + 1, curSum + nums[i])
            dfs(i + 1, curSum - nums[i])
            return

        dfs(0, 0)
        return res[0]

    def findTargetSumWaysV2(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> number of ways to get target

        def backtracking(i, total):
            # 返回值代表:
            # 在第i个位置， 且0到i位置的数操作后的值为total时，剩余的数据有多少个种组合，可以使得总的操作等于target
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtracking(i + 1, total + nums[i]) +
                              backtracking(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtracking(0, 0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    s = Solution()

    a = s.findTargetSumWaysV2(nums, target)
    print(a)

    nums = [22, 25, 21, 8, 32, 36, 26, 22, 12, 26, 32, 1, 11, 21, 19, 50, 2, 1, 19, 32]
    target = 24
    a = s.findTargetSumWays(nums, target)

    aa = s.findTargetSumWaysV2(nums, target)
    print(a, aa)
