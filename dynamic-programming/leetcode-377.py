from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # key(ie target)  -> number of combination to get target use nums list
        dp = {0: 1}  # 一个都不选是1种组合方法，可以得到target=0

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)

        return dp[total]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4

    s = Solution()
    a = s.combinationSum4(nums, target)
    print(a)

    nums = [9]
    target = 3
    a = s.combinationSum4(nums, target)
    print(a)
