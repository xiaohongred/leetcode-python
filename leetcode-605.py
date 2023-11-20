from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbedLen = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        for cur in range(1, flowerbedLen + 1):
            pre = cur - 1
            next = cur + 1
            if flowerbed[pre] == 0 and flowerbed[next] == 0 and flowerbed[cur] == 0:
                n -= 1
                flowerbed[cur] = 1

            if n == 0:
                return True

        if n > 0:
            return False
        return True


if __name__ == '__main__':
    pass
