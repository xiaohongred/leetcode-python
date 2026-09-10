from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalPoints = sum(cardPoints)
        if k == len(cardPoints):
            return totalPoints
        minRemoveTotal = float('inf')
        totalK = 0
        K = len(cardPoints) - k
        for i, n in enumerate(cardPoints):
            left = i - K + 1
            totalK += n
            if left < 0:
                continue

            minRemoveTotal = min(minRemoveTotal, totalK)
            totalK -= cardPoints[left]
        return totalPoints - minRemoveTotal


if __name__ == "__main__":
    s = Solution()
    print(s.maxScore([1,2,3,4,5,6,1], 3))

    cardPoints = [2,2,2]
    k = 2
    print(s.maxScore(cardPoints, k))

    cardPoints = [9,7,7,9,7,7,9]
    k = 7
    print(s.maxScore(cardPoints, k))