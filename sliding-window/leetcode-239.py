import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index

        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:  # 保证 q 队列是单调递减的
                q.pop()
            q.append(r)

            # remove left val from window
            # 用　while 也可以
            if l > q[0]:  # q[0] 代表nums中最左侧的元素的索引，如果 l > q[0],则代表窗口已经不包括 nums[q[0]] 这个数了，需要出队列
                q.popleft()

            if (r + 1) >= k:  # 从 nums 数组的第 k 个数开始，每次都需要往output数组中赋值了
                output.append(nums[q[0]])
                l += 1  # 窗口右移

            r += 1  # 窗口右移
        return output

    def maxSlidingWindowV1(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index

        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:  # 保证 q 队列是单调递减的
                q.pop()
            q.append(r)

            # remove left val from window
            while l > q[0]:  # q[0] 代表nums中最左侧的元素的索引，如果 l > q[0],则代表窗口已经不包括 nums[q[0]] 这个数了，需要出队列
                q.popleft()

            if (r + 1) >= k:  # 从 nums 数组的第 k 个数开始，每次都需要往output数组中赋值了
                output.append(nums[q[0]])
                l += 1  # 窗口右移

            r += 1  # 窗口右移
        return output

    # 时间超出限制
    def maxSlidingWindowV0(self, nums: List[int], k: int) -> List[int]:
        res = []

        def findMax(l, r):
            tmpMax = -1 * float("inf")
            for i in range(l, r + 1):
                tmpMax = max(tmpMax, nums[i])
            return tmpMax

        l = 0
        r = k - 1
        while r < len(nums):
            res.append(findMax(l, r))
            l += 1
            r += 1
        return res


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    a = solu.maxSlidingWindow(nums, k)
    print(a)

    nums = [1]
    k = 1
    a = solu.maxSlidingWindow(nums, k)
    print(a)

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    a = solu.maxSlidingWindowV0(nums, k)
    print(a)

    nums = [1]
    k = 1
    a = solu.maxSlidingWindowV0(nums, k)
    print(a)
