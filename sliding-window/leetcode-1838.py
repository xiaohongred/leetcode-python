from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # sort nums
        l, r = 0, 0
        res, total = 0, 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 4]
    k = 5
    a = solu.maxFrequency(nums, k)
    print(a)

    nums = [1, 4, 8, 13]
    k = 5
    a = solu.maxFrequency(nums, k)
    print(a)

    nums = [3, 9, 6]
    k = 2
    a = solu.maxFrequency(nums, k)
    print(a)
