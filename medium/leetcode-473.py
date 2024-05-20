from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        allSum = sum(matchsticks)
        if allSum % 4:
            return False
        oneSideLen = allSum // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def backtrack(i):  # 第i个火柴
            if i == len(matchsticks):
                return True
            for j in range(len(sides)):
                if sides[j] + matchsticks[i] <= oneSideLen:
                    sides[j] = sides[j] + matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] = sides[j] - matchsticks[i]
            return False

        return backtrack(0)


if __name__ == '__main__':
    matchsticks = [1, 1, 2, 2, 2]
    s = Solution()
    a = s.makesquare(matchsticks)
    print(a)

    matchsticks = [3, 3, 3, 3, 4]
    a = s.makesquare(matchsticks)
    print(a)
