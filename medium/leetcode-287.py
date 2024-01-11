from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> float:
        slow, fast = 0, 0
        while 1:
            fast = nums[fast]
            fast = nums[fast]

            slow = nums[slow]
            if slow == fast:
                break

        slow = 0
        while 1:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break

        return fast

    def findDuplicateV2(self, nums: List[int]) -> float:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]

            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    s = Solution()
    a = s.findDuplicate(nums)
    print(a)
