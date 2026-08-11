from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        print(LIS)
        return max(LIS)

    # 内存超限
    def lengthOfLISV2(self, nums: List[int]) -> int:
        cache = {}

        def dfs(nums: List[int], index: int, curMax: int) -> int:
            if index > len(nums) - 1:
                return 0

            if (index, curMax) in cache:
                return cache[(index, curMax)]

            if nums[index] > curMax:
                cache[(index, curMax)] = max(
                    1 + dfs(nums, index + 1, nums[index]), dfs(nums, index + 1, curMax)
                )
            else:
                cache[(index, curMax)] = dfs(nums, index + 1, curMax)

            return cache[(index, curMax)]

        return dfs(nums, 0, float('-inf'))


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    a = s.lengthOfLIS(nums)
    print(a)
