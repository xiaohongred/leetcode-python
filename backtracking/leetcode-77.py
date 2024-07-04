from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int, comb: List[int]):
            if len(comb) == k:
                res.append(comb.copy())
            if len(comb) > k:
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
            return

        backtrack(1, path)
        return res


if __name__ == '__main__':
    n = 4
    k = 2

    s = Solution()
    a = s.combine(n, k)
    print(a)
