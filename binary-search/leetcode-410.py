from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = {}

        def dfs(i, k):  # 从nums[i]开始, 把数组分成k份，使得每份的和的最大值 最小，怎么分，dfs 的返回值是最小的 最大和
            if k == 1:
                return sum(nums[i:])
            if (i, k) in dp:
                return dp[(i, k)]
            res, curSum = float("inf"), 0
            for j in range(i, len(nums) - k + 1):
                curSum += nums[j]
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
            for n in nums:  # largest 代表每份 和的最大值
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= k  # 如果按照每份和的最大值<largest,的要求，分出来的份数 <= k, 则认为可分

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
    s = Solution()

    nums = [7, 2, 5, 10, 8]
    k = 2
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
