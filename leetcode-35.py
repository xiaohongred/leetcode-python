from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        numsLen = len(nums)
        l = 0
        r = numsLen - 1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if l > (numsLen - 1):
            return numsLen

        if r < 0:
            return 0

        return l



if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,6]
    target = 6
    a = s.searchInsert(nums, target)
    print(a)