from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positiveSet = set()
        maxPos = -1
        for num in nums:
            if num >= 0:
                positiveSet.add(num)
                maxPos = max(maxPos, num)
        if len(positiveSet) == 0:
            return 1
        for i in range(1, maxPos + 1):
            if i not in positiveSet:
                return i
        return maxPos + 1

    def firstMissingPositiveV2(self, nums: List[int]) -> int:
        # 把负数都改为0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        # 使用输入的 nums 作为存储空间
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:  # mean val = i  never show in nums
                return i
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 0]
    a = s.firstMissingPositive(nums)
    print(a)

    nums = [3, 4, -1, 1]
    a = s.firstMissingPositive(nums)
    print(a)

    nums = [7, 8, 9, 11, 12]
    a = s.firstMissingPositive(nums)
    print(a)

    nums = [1, 2, 0]
    a = s.firstMissingPositiveV2(nums)
    print(a)

    nums = [3, 4, -1, 1]
    a = s.firstMissingPositiveV2(nums)
    print(a)

    nums = [7, 8, 9, 11, 12]
    a = s.firstMissingPositive(nums)
    print(a)
