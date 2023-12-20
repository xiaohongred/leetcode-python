from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if target == nums[mid]:
                return mid

            # mid in left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    s = Solution()
    a = s.search(nums, target)
    print(a)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    a = s.search(nums, target)
    print(a)
