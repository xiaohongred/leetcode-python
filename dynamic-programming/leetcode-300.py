from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        LIS[-1] = 1  # LIS[i] 代表从nums[i] 开始， 到nums数组最后的最长子序列
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    s = Solution()

    a = s.lengthOfLIS(nums)
    print(a)

    nums = [0, 1, 0, 3, 2, 3]
    a = s.lengthOfLIS(nums)
    print(a)
