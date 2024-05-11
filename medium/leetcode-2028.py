from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        mSum = sum(rolls)
        nSum = (n + m) * mean - mSum
        if nSum < n or nSum > n * 6:
            return []
        nMean = nSum // n
        # if nMean < 1 or nMean > 6:
        #     return []
        res = [nMean] * n
        remain = nSum % n
        for i in range(remain):
            res[i] += 1
            if res[i] > 6:
                return []
        return res


if __name__ == '__main__':
    rolls = [3, 2, 4, 3]
    mean = 4
    n = 2
    s = Solution()
    a = s.missingRolls(rolls, mean, n)
    print(a)
