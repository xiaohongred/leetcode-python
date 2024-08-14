from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        allSum = sum(nums)
        if allSum % 2:
            return False
        target = allSum // 2
        cache = {}

        def dfs(i, target):
            if target == 0:
                return True
            if target < 0:
                return False
            if i >= len(nums):
                return False
            if (i, target) in cache:
                return cache[(i, target)]
            res = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            cache[(i, target)] = res
            return res

        return dfs(0, target)

    def canPartitionDP(self, nums: List[int]) -> bool:
        allSum = sum(nums)
        if allSum % 2:
            return False
        target = allSum // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        if target in dp:
            return True
        return False


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    s = Solution()
    a = s.canPartition(nums)
    print(a)

    nums = [1, 2, 3, 5]
    a = s.canPartition(nums)
    print(a)
