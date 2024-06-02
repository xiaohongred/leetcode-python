# https://www.lintcode.com/problem/508/

from typing import (
    List,
)


class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """

    def wiggle_sort(self, nums: List[int]):
        # write your code here
        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

            if i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

        return
