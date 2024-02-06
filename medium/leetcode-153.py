from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    s = Solution()
    a = s.findMin(nums)
    print(a)
