from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = [0]

        def dp(curSum, target):
            if curSum == target:
                res[0] = res[0] + 1
                return
            if curSum > target:
                return
            for n in nums:
                dp(curSum + n, target)
            return

        dp(0, target)
        return res[0]

    def combinationSum4_V2(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)

        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    s = Solution()
    a = s.combinationSum4_V2(nums, target)
    print(a)
