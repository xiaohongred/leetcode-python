from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur: List[int], pos: int, target: int):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])  # 取当前值

                backtrack(cur, i + 1, target - candidates[i])

                cur.pop()  # 不取当前值

                prev = candidates[i]  # 记录前一个数

        backtrack([], 0, target)
        return res


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    s = Solution()
    a = s.combinationSum2(candidates, target)
    print(a)
