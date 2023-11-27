from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [n * n for n in nums]

        if nums[-1] <= 0:
            return [nums[i] * nums[i] for i in range(len(nums) - 1, -1, -1)]

        l, r = -1, -1
        for i in range(len(nums) - 1):
            if nums[i] <= 0 and nums[i + 1] > 0:
                l = i
                r = i + 1
                break
        res = []
        while l >= 0 and r <= (len(nums) - 1):
            if nums[l] * nums[l] < nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l -= 1
            else:
                res.append(nums[r] * nums[r])
                r += 1

        while l >= 0:
            res.append(nums[l] * nums[l])
            l -= 1

        while r <= len(nums) - 1:
            res.append(nums[r] * nums[r])
            r += 1
        return res

    def sortedSquaresV2(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        return res[::-1]  # reverse


if __name__ == '__main__':
    pass
