from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    a = s.rearrangeArray(nums)
    print(a)
