from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = -1
        for r in range(0, len(nums)):
            if nums[r] != val:
                l += 1
                nums[l] = nums[r]

        return l + 1


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    target = 2
    s = Solution()
    a = s.removeElement(nums, target)
    print(nums, a)
