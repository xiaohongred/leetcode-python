from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numToCount = Counter(nums)

        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * numToCount[nums[i]]
            # can not use both curEarn and earn2
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2


if __name__ == '__main__':
    nums = [3, 4, 2]
    s = Solution()
    a = s.deleteAndEarn(nums)
    print(a)
