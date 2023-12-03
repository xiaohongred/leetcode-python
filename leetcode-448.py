from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mySet = set()
        for n in nums:
            mySet.add(n)

        res = []
        for i in range(1, len(nums) + 1):
            if i in mySet:
                continue
            else:
                res.append(i)
        return res

    def findDisappearedNumbersV2(self, nums: List[int]) -> List[int]:
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.findDisappearedNumbers(nums))
