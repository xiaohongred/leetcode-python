from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def subsets_Backtrack(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def backtrack(start, path):
            res.append(path.copy())  # 每个节点都是答案。

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, subset)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    a = s.subsets_Backtrack(nums)
    print(a)

    b = s.subsets(nums)
    print(a)
