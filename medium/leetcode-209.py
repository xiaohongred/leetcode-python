from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l = 0
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= target:
                res = min(res, i - l + 1)
                curSum -= nums[l]
                l += 1
        if res == float("inf"):
            return 0
        return res


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    s = Solution()
    a = s.minSubArrayLen(target, nums)
    print(a)
