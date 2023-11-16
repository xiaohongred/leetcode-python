from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        nums.sort()
        print(nums)
        for n in nums:
            if n in mySet:
                return True

            mySet.add(n)

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    a = s.containsDuplicate(nums)
    print(a)
