from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                index = mid
                break
        if index == -1:
            return res
        l, r = index, index
        while l >= 0 and nums[l] == target:
            res[0] = l
            l -= 1

        while r < len(nums) and nums[r] == target:
            res[1] = r
            r += 1
        return res

    def searchRangeV2(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.binSearch(nums, target, True)
        res[1] = self.binSearch(nums, target, False)
        return res

    # leftBias = [True/False], if false, res is rightBiased
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
                if leftBias:  # 如果是要找最左边的元素
                    r = mid - 1
                else:  # 如果是要找最右边的元素
                    l = mid + 1
        return i


if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    a = s.searchRange(nums, target)
    print(a)

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    a = s.searchRange(nums, target)
    print(a)

    nums = []
    target = 0
    a = s.searchRange(nums, target)
    print(a)

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    a = s.searchRangeV2(nums, target)
    print(a)

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    a = s.searchRangeV2(nums, target)
    print(a)

    nums = []
    target = 0
    a = s.searchRangeV2(nums, target)
    print(a)
