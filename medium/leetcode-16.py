from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # a b c 三个数分别对应nums[i]  nums[j] nums[k]
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果 s > target, 移动c 的指针
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1

                    k = k0
                else:
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    a = s.threeSumClosest(nums, target)
    print(a)

    nums = [0, 0, 0]
    target = 1
    a = s.threeSumClosest(nums, target)
    print(a)
