from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and nums[i] != 0:
            i += 1

        if i >= len(nums) - 1:
            return

        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1

    def moveZerosV2(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZerosV2(nums)
    print(nums)
