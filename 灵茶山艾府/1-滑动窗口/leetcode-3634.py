from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # 排序后，保留下来的元素一定是连续一段：
        # 只要 max <= min * k，多留元素永远不会让条件变差
        nums.sort()
        n = len(nums)
        ans = 1                     # 至少能只留 1 个元素（单个元素一定平衡）
        left = 0
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1           # 最小值太小，收缩左边界
            ans = max(ans, right - left + 1)
        return n - ans


if __name__ == "__main__":
    s = Solution()
    print(s.minRemoval([2, 1, 5], 2))        # 1
    print(s.minRemoval([1, 6, 2, 9], 3))     # 2
    print(s.minRemoval([4, 6], 2))           # 0
    print(s.minRemoval([5], 100))            # 0
    print(s.minRemoval([1, 2, 3, 4, 5], 1))  # 4  (k=1 时要求所有元素相等，只能留 1 个)
