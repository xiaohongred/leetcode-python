from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
            else:
                res -= nums[i]

        return res

    def singleNumberV2(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n

        return res


if __name__ == '__main__':
    pass
