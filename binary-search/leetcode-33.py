from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:  # currnet mid in left sorted portion ,if [l, r] has pivot
                if target > nums[mid] or target < nums[l]:
                    # 1. target > nums[mid] 代表target 可能 在 左半部份
                    # 2. target < nums[l]  代表target 可能 在 右半部份
                    # 由于此时 mid 在左半部分， 所以 l 应该到 mid+1的位置来
                    #   这样 [l, r] 的范围就包含了 1,2 两种情况
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # mid in right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

    def searchV2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # 旋转位置称为pivot
        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid
            # 如果[l, r] 之间不包括 pivot 点， 就是正常的 二分查找
            # 一直缩小 [l, r] 的区间， 直到 r > l ,跳出循环
            if nums[l] <= nums[mid]:  # 如果 [l, r] 之间包括了 pivot, nums[l] <= nums[mid] 代表 mid 在 pivot的左侧
                if target > nums[mid]:
                    # 如果 [l, r] 之间包括了 pivot, target 可能在 mid 到 pivot 之间,
                    # 如果 [l, r] 之间不包括了 pivot, 则 target 可能在 mid 到 r之间
                    l = mid + 1
                elif target < nums[l]:
                    # 如果 [l, r] 之间包括了 pivot, target可能在 pivot 到 r 之间
                    # 如果 [l, r] 之间不包括了 pivot, 不可能进入这个分支
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # 如果 [l, r] 之间包括了 pivot， 进入这个 else 代表 mid 在 pivot的右侧, right side
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    a = s.search(nums, target)
    print(a)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    a = s.search(nums, target)
    print(a)

    nums = [1]
    target = 0
    a = s.search(nums, target)
    print(a)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    a = s.searchV2(nums, target)
    print(a)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    a = s.searchV2(nums, target)
    print(a)

    nums = [1]
    target = 0
    a = s.searchV2(nums, target)
    print(a)
