from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1  # cancel  i+=1,   nums[r] might be zero
            i += 1


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(nums)
    s = Solution()
    s.sortColors(nums)
    print(nums)
