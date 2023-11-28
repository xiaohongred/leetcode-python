from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        allSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = allSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    s = Solution()
    a = s.pivotIndex(nums)
    print(a)
