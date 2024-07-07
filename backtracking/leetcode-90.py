from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i: int, subset: List[int]):
            if i == len(nums):
                res.append(subset.copy())
                return

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # skip duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # all subsets that not include nums[i]
            backtrack(i + 1, subset)

        path = []
        backtrack(0, path)
        return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    s = Solution()
    a = s.subsetsWithDup(nums)
    print(a)

    nums = [0]
    a = s.subsetsWithDup(nums)
    print(a)
