from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}  # val: index
        for idx, item in enumerate(nums):
            diff = target - item
            if diff in hmap:
                return [hmap[diff], idx]
            hmap[item] = idx


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    a = s.twoSum(nums, target)
    print(a)
