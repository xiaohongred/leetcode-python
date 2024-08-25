from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = {}

        def dfs(i, k):  # 从nums的i位置开始到数组末尾，分成k份，这 k 个非空的连续子数组 各自和 的最大值最小是dfs的返回值
            if k == 1:
                return sum(nums[i:])
            if (i, k) in dp:
                return dp[(i, k)]

            res, curSum = float("inf"), 0
            for j in range(i, len(nums) - k + 1):  # 从i 到 j, 当作一个连续的子数组，剩余的部分就需要再分成 k - 1份
                curSum += nums[j]  # 从i 到 j, 当作一个连续的子数组,累加和是 curSum
                maxSum = max(curSum, dfs(j + 1, k - 1))
                res = min(res, maxSum)
                if curSum > res:
                    break

            dp[(i, k)] = res
            return res

        return dfs(0, k)

    def splitArrayV2(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n

            return subarray + 1 <= k  # 每份的累加和最大能够到 largest， 可以分成 subarray + 1 份, k是题目要求的份数

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    k = 2

    s = Solution()
    a = s.splitArray(nums, k)
    print(a)

    nums = [1, 2, 3, 4, 5]
    k = 2
    a = s.splitArray(nums, k)
    print(a)

    nums = [1, 4, 4]
    k = 3
    a = s.splitArray(nums, k)
    print(a)

    nums = [7, 2, 5, 10, 8]
    k = 2
    a = s.splitArrayV2(nums, k)
    print(a)

    nums = [1, 2, 3, 4, 5]
    k = 2
    a = s.splitArrayV2(nums, k)
    print(a)

    nums = [1, 4, 4]
    k = 3
    a = s.splitArrayV2(nums, k)
    print(a)
