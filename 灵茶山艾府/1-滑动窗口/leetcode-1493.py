from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 滑动窗口：窗口内 0 的个数 <= 1，窗口长度减 1 就是删掉那个 0 后的全 1 长度
        ans = 0
        left = 0
        zeros = 0
        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1
            while zeros > 1:          # 窗口不合法，收缩左边界
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans - 1                # 必须删掉一个元素（全 1 时删掉一个 1）

    def longestSubarrayV2(self, nums: List[int]) -> int:
        mySet = set()
        ans = 0
        left = 0
        for right, n in enumerate(nums):
            if n == 1:
                ans = max(ans, right - left + 1)
            else:
                if len(mySet) == 0:
                    mySet.add(right)
                    ans = max(ans, right - left + 1)   # 必须是窗口长度，和 n == 1 分支统一
                else:
                    while nums[left] == 1:
                        left += 1
                    if left == right:
                        mySet.clear()
                    left += 1
                    ans = max(ans, right - left + 1)
        return ans - 1


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([1,1,0,1]))  # 3
    print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))  # 5
    print(s.longestSubarray([1,1,1]))  # 2
    print(s.longestSubarray([1,1,0,0,1,1,1,0,1]))  # 4
    print(s.longestSubarray([0,0,0]))  # 0