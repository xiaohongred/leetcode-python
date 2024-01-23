from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    s = Solution()
    a = s.subarraySum(nums, k)
    print(a)
