from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}  # map remainder -> end index

        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6

    s = Solution()
    a = s.checkSubarraySum(nums, k)
    print(a)
