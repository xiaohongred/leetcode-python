from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # sets = set()
        # for n in nums:
        #     sets.add(n)
        sets = set(nums)
        
        for i in range(1, 10000):
            if i*k in sets:
                continue
            else:
                return i*k
        return None

    def missingMultipleV2(self, nums: List[int], k: int) -> int:
        sets = set(nums)
        
        ans = k
        while ans in sets:
            ans += k
        
        return ans


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(so.missingMultiple(nums, k))

    nums = [1,4,7,10,15]
    k = 5
    print(so.missingMultiple(nums, k))