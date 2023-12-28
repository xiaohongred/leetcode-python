from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    a = s.canJump(nums)
    print(a)
