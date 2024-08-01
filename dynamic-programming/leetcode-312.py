from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # 两边各加一个1

        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]  # 最后才戳破第i个气球
                coins += dfs(l, i - 1) + dfs(i + 1, r)  # 最后戳破第i个气球获得的硬币 + 戳破 第i个气球的左右两边的气球获得的硬币
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    s = Solution()
    a = s.maxCoins(nums)
    print(a)

    nums = [1, 5]
    a = s.maxCoins(nums)
    print(a)
