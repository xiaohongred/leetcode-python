from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack(index):
            result.append(path.copy())
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(i + 1)
                path.pop()
                used[i] = False
            return

        backtrack(0)
        return result

    def subsetsWithDupV2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # all subsets that do not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
            return

        backtrack(0, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    s = Solution()
    a = s.subsetsWithDup(nums)
    print(a)

    nums = [0]
    a = s.subsetsWithDup(nums)
    print(a)
