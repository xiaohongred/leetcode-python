from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                # l, r 之间，最后才刺破位置 i 的气球
                # 最后刺破i位置的气球能获得的硬币数
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                # 刺破除了i之外的其他气球，能获得的最大硬币数是  dfs(l, i - 1) + dfs(i + 1, r)
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 5, 8]
    a = s.maxCoins(nums)
    print(a)

    nums = [1, 5]
    a = s.maxCoins(nums)
    print(a)
