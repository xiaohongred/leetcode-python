from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1

        return i


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    s = Solution()
    a = s.searchRange(nums, target)
    print(a)
