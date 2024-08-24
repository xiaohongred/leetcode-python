from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dynamic programming
        dp = {}  # key = index, value=[length of LIS, count]
        lenLIS, res = 0, 0  # length of LIS, count of LIS
        # i = start of subreq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1  # len, cnt of LIS start from i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:  # make sure increasing order
                    length, count = dp[j]  # len, cnt of LIS start from j
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    s = Solution()
    a = s.findNumberOfLIS(nums)
    print(a)

    nums = [2, 2, 2, 2, 2]
    a = s.findNumberOfLIS(nums)
    print(a)
