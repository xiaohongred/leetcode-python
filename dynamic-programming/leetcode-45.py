from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:  # r == (len(nums)-1) 时退出循环，因为到达了最后一个位置
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    a = s.jump(nums)
    print(a)

    nums = [2, 3, 0, 1, 4]
    a = s.jump(nums)
    print(a)
