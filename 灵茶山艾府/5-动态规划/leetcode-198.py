from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:   # 回溯写法  会超时
        n = len(nums)

        def dfs(i):
            if i < 0:
                return 0
            res = max(dfs(i-1), dfs(i-2) + nums[i])
            return res
        return dfs(n-1)

    def robWithCache(self, nums: List[int]) -> int:   # 回溯写法  + Cache
        n = len(nums)

        cache = [-1] * n
        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            res = max(dfs(i-1), dfs(i-2) + nums[i])
            cache[i] = res
            return res
        return dfs(n-1)

    def robV2(self, nums: List[int]) -> int:   # 动态规划写法
        n = len(nums)
        f = [0] * (n + 2)   # 可以看做在数组前面加了两个 0，方便处理边界条件
        for i, x in enumerate(nums):
            f[i+2] = max(f[i+1], f[i] + x)   # f[i] = max(f[i-1], f[i-2] + nums[i])  这里的 i 是从 0 开始的，所以要加 2
        return f[n+1]
    def robV3(self, nums: List[int]) -> int:   # 动态规划写法 进一步节省空间
        n = len(nums)
        f0, f1 = 0, 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)   # f[i] = max(f[i-1], f[i-2] + nums[i])  这里的 i 是从 0 开始的，所以要加 2
        return f1