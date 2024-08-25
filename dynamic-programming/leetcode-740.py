import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        numToCount = collections.defaultdict(int)  # num: cnt of num
        for n in nums:
            numToCount[n] += 1

        nums = sorted(list(set(nums)))  # 去重，排序

        earn1, earn2 = 0, 0
        #   e1  e2
        #   [1, 2, 3]
        # [0 1 2 3]
        for i in range(len(nums)):
            curEarn = nums[i] * numToCount[nums[i]]
            # can not use both curEarn and earn2
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                # 前一个元素不可用,因为 nums[i] == nums[i - 1] + 1，
                # 两个选择选其中一个
                # 一个是用当前元素+前前一个元素 -> curEarn + earn1
                # 另一个是使用 前一个元素 -> earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2  # 前一个元素也可用
                earn1 = temp
        return earn2

    def deleteAndEarnV2(self, nums: List[int]) -> int:
        numToCount = collections.Counter(nums)

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

    a = s.deleteAndEarnV2(nums)
    print(a)

    nums = [2, 2, 3, 3, 3, 4]
    a = s.deleteAndEarn(nums)
    print(a)

    a = s.deleteAndEarnV2(nums)
    print(a)
