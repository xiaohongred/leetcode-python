from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: List[int], total: int):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)

        path = []
        dfs(0, path, 0)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7

    s = Solution()
    a = s.combinationSum(candidates, target)
    print(a)
