from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(total, res)
            r += 1
            l += 1
        return res


if __name__ == '__main__':
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3

    s = Solution()
    a = s.maxScore(cardPoints, k)
    print(a)
