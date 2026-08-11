from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    def robV2(self, nums: List[int]) -> int:
        cache = {}

        def dp(nums: List[int], index: int) -> int:
            if index > len(nums) - 1:
                return 0

            if index in cache:
                return cache[index]

            cache[index] = max(nums[index] + dp(nums, index + 2), dp(nums, index + 1))
            return cache[index]

        return dp(nums, 0)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    a = s.rob(nums)
    print(a)
