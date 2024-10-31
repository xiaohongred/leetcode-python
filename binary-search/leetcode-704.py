from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = r - 1
            elif nums[mid] < target:
                l = l + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    a = s.search(nums, target)
    print(a)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    a = s.search(nums, target)
    print(a)
