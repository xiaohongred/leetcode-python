from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # 两边各加一个元素1

        dp = {}  # dp[(l, r)] 代表在 l, r 这个区间的 nums 数组中， 戳破这些气球能够获得的最大硬币数

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                # 在l, r 区间中，最后才戳破第i个气球, 在戳破第i个气球之前， l,r区间中的其他气球都被戳破了
                # 所以才有 nums[l - 1] * nums[i] * nums[r + 1]
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                # 最后戳破第i个气球获得的硬币(coins) + 戳破第i个气球的左右两边的气球获得的硬币(dfs(l, i - 1) + dfs(i + 1, r))
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        res = dfs(1, len(nums) - 2)
        return res


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    s = Solution()
    a = s.maxCoins(nums)
    print(a)

    nums = [1, 5]
    a = s.maxCoins(nums)
    print(a)
