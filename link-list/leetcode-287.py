from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
            if slow2 == slow:
                break
        return slow

    def findDuplicateV2(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                break
        return slow


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 4, 2, 2]
    a = s.findDuplicate(nums)
    print(a)

    nums = [3, 1, 3, 4, 2]
    a = s.findDuplicate(nums)
    print(a)

    nums = [3, 3, 3, 3, 3]
    a = s.findDuplicate(nums)
    print(a)
