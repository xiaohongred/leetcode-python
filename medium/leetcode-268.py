from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        should = (n + 0) * (n + 1) / 2
        realSum = sum(nums)
        return int(should - realSum)


if __name__ == '__main__':
    nums = [3, 0, 1]
    s = Solution()
    a = s.missingNumber(nums)
    print(a)
