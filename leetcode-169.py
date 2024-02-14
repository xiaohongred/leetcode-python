from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res

    def majorityElementV2(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if res == n:
                count += 1
            else:
                count -= 1
                if count < 0:
                    res = n
                    count = 0

        return res

    def majorityElementV21(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res


if __name__ == '__main__':
    s = Solution()

    nums = [3, 2, 3]
    print(s.majorityElement(nums))
