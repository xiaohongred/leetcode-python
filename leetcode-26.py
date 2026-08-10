from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen == 1:
            return 1
        i = 0  # 指向第一个唯一元素
        j = 1  # 遍历元素
        while j < numLen:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1  # nums[i] != nums[j] 时， 增加i,并把 nums[j] 前移到 nums[i]
                nums[i] = nums[j]
                j += 1

        return i + 1

    def removeDuplicatesV2(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen == 1:
            return 1

        l, r = 1, 1
        while r < numLen:
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l

    def removeDupV3(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 6]
    s = Solution()
    a = s.removeDuplicatesV2(nums)
    print(nums)
    print(a)
