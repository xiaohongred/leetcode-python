class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    a = s.rob(nums)
    print(a)
