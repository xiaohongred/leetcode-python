from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res


if __name__ == '__main__':
    nums = [90]
    k = 1

    s = Solution()
    a = s.minimumDifference(nums, k)
    print(a)
    nums = [9, 4, 1, 7]
    k = 2
    a = s.minimumDifference(nums, k)
    print(a)
