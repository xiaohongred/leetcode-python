from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                res = max(res, mid + 1)
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
        return res if res > 0 else 0

    def searchInsertV2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    s = Solution()

    nums = [1, 3, 5, 6]
    target = 5
    a = s.searchInsert(nums, target)
    print(a)

    nums = [1, 3, 5, 6]
    target = 2
    a = s.searchInsert(nums, target)
    print(a)

    nums = [1, 3, 5, 6]
    target = 7
    a = s.searchInsert(nums, target)
    print(a)

    nums = [1, 3, 5, 6]
    target = 5
    a = s.searchInsertV2(nums, target)
    print(a)

    nums = [1, 3, 5, 6]
    target = 2
    a = s.searchInsertV2(nums, target)
    print(a)

    nums = [1, 3, 5, 6]
    target = 7
    a = s.searchInsertV2(nums, target)
    print(a)
