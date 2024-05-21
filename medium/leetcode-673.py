from typing import List


class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        # LIS longest increase subseq
        dp = {}  # key = index, value=[length of LIS, count]
        lenLIS, res = 0, 0
        # i = start of subreq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1  # len, cnt of LIS start from index i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count

            dp[i] = [maxLen, maxCnt]
            # update res
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    s = Solution()
    a = s.findNumberOfLIS(nums)
    print(a)
    nums = [2, 2, 2, 2, 2]
    a = s.findNumberOfLIS(nums)
    print(a)
