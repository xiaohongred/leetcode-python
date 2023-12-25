from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)
            return

        path = []
        dfs(0, path, 0)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8

    s = Solution()
    a = s.combinationSum(candidates, target)
    print(a)
