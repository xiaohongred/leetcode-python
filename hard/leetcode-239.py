import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        l = r = 0
        q = collections.deque()  # index
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove left val from window
            if l > q[0]:
                q.popleft()
            if (r - l + 1) >= k:  # 窗口宽度大于等于k时，要看结果
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    a = s.maxSlidingWindow(nums, k)
    print(a)

    nums = [1]
    k = 1
    a = s.maxSlidingWindow(nums, k)
    print(a)
