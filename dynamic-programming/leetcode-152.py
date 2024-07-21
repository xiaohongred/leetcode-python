from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            tmp = curMax * n
            curMax = max(curMin * n, curMax * n, n)
            curMin = min(curMin * n, tmp, n)
            res = max(res, curMax)
        return res


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    s = Solution()
    a = s.maxProduct(nums)
    print(a)
