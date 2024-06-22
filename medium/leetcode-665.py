from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # wrong
        # cnt = 0
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         cnt += 1
        # if cnt > 1:
        #     return False
        # return True
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            # we want to decrease left element
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True


if __name__ == '__main__':
    nums = [4, 2, 3]
    s = Solution()
    a = s.checkPossibility(nums)
    print(a)

    nums = [4, 2, 1]
    a = s.checkPossibility(nums)
    print(a)

    nums = [3, 4, 2, 3]
