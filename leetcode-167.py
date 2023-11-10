from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            curSum = numbers[i] + numbers[j]
            if (curSum > target):
                j = j - 1
            elif (curSum < target):
                i = i + 1
            else:
                return [i + 1, j + 1]

        return []


if __name__ == '__main__':
    km = {"golad": "12"}
    for k, v in km.items():
        print(k, v)

