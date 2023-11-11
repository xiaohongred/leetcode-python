from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rMax = -1
        index = len(arr) - 1
        while index >= 0:
            tmp = arr[index]
            arr[index] = rMax
            rMax = max(rMax, tmp)
            index -= 1

        return arr

    def replaceElementsV2(self, arr: List[int]) -> List[int]:
        rMax = -1
        index = len(arr) - 1
        while index >= 0:
            newMax = max(rMax, arr[index])
            arr[index] = rMax
            rMax = newMax
            index -= 1

        return arr


if __name__ == '__main__':
    s = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    print(s.replaceElementsV2(arr))
