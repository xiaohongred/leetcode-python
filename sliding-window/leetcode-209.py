from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float("inf") else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]

    s = Solution()
    a = s.minSubArrayLen(target, nums)
    print(a)

    target = 4
    nums = [1, 4, 4]
    a = s.minSubArrayLen(target, nums)
    print(a)

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    a = s.minSubArrayLen(target, nums)
    print(a)
