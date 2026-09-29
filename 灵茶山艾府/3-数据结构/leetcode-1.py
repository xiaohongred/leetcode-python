class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx = {}

        for j, x in enumerate(nums):
            if target - x in idx:
                return [idx[target-x], j]
            idx[x] = j
        return

# 0.1 枚举右，维护左
# https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(s.twoSum([3, 2, 4], 6))       # [1, 2]
    print(s.twoSum([3, 3], 6))          # [0, 1]