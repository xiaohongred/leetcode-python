from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(cur: List[int], pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    s = Solution()
    a = s.combinationSum2(candidates, target)
    print(a)
