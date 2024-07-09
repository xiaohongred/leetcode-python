from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways to get target val start at index, curTotal is total

        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtrack(0, 0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    s = Solution()
    a = s.findTargetSumWays(nums, target)
    print(a)
