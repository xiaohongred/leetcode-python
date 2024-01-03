from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        prefix = [0] * numLen
        postfix = [0] * numLen

        sumM = 1
        for i in range(numLen):
            sumM *= nums[i]
            prefix[i] = sumM

        sumM = 1
        for i in range(numLen - 1, -1, -1):
            sumM *= nums[i]
            postfix[i] = sumM

        res = [0] * numLen
        for i in range(numLen):
            if i == 0 and i + 1 < numLen:
                res[i] = postfix[i + 1]
                continue

            if i == numLen - 1 and i - 1 >= 0:
                res[i] = prefix[i - 1]
                continue

            res[i] = postfix[i + 1] * prefix[i - 1]
        return res

    def productExceptSelfV2(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        res = [1] * numLen
        prefix = 1
        for i in range(numLen):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    a = s.productExceptSelf(nums)
    print(a)

    a = s.productExceptSelfV2(nums)
    print(a)
