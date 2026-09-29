
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        题意：删除数组中的**一个**元素后，返回最长的全为 1 的子数组长度。
        等价转换：找出一个最长的连续区间，其中 0 的个数不超过 1 个。
        因为区间里最多只有一个 0 时，删掉它（或者删掉一个 1）就能让剩下的全是 1。

        思路：不定长滑动窗口（同向双指针）
        - 窗口 [left, right] 内始终保持「0 的个数 <= 1」这个性质。
        - right 负责向右扩张窗口，每步把新元素纳入窗口。
        - 一旦窗口内 0 的个数超过 1，就让 left 向右收缩，直到窗口重新合法。
        - 每次窗口合法后，用窗口长度更新答案。

        时间复杂度 O(n)：right 和 left 各自最多走 n 步。
        空间复杂度 O(1)：只用了常数个变量。
        """
        left = 0          # 窗口左边界（包含）
        zero_count = 0    # 当前窗口 [left, right] 内 0 的个数
        max_length = 0    # 记录所有合法窗口中的最大长度

        # right 是窗口右边界，负责向右扩张
        for right in range(len(nums)):
            # 把 nums[right] 纳入窗口，维护 0 的计数
            if nums[right] == 0:
                zero_count += 1

            # 若窗口内 0 超过 1 个，则窗口不合法，需要从左边收缩
            # 用 while 而不是 if，是因为可能要移动很多步才能去掉多余的 0
            while zero_count > 1:
                # 如果左边出去的元素是 0，0 的计数要减 1
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # 左边界右移

            # 此时窗口 [left, right] 内至多有一个 0，是合法的
            # 窗口长度为 right - left + 1
            max_length = max(max_length, right - left + 1)

        # 题目要求「必须删除一个元素」，所以最终结果要减 1。
        # 注意：即使整个数组全是 1（max_length == n），删掉一个后长度也是 n - 1，逻辑一致。
        return max_length - 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 0, 1]
    result = solution.longestSubarray(nums)
    print(result)  # Output: 3

    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    result = solution.longestSubarray(nums)
    print(result)  # Output: 5

    nums = [1, 1, 1]
    result = solution.longestSubarray(nums)
    print(result)  # Output: 2