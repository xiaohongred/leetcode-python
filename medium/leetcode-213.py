from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        r1 = self.helper(nums[1:])
        r2 = self.helper(nums[:len(nums) - 1])
        return max(r1, r2)

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2


if __name__ == '__main__':
    nums = [2, 3, 2]
    s = Solution()
    a = s.rob(nums)
    print(a)
