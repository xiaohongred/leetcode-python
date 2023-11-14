from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen == 1:
            return 1
        i = 0
        j = 1
        while j < numLen:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

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


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 6]
    s = Solution()
    a = s.removeDuplicatesV2(nums)
    print(nums)
    print(a)
