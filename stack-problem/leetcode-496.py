from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:  # 只处理 nums1 中出现的数
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]  # idx 为 nums2[i] 在 nums1 中的索引
                    res[idx] = nums2[j]
                    break
        return res

    def nextGreaterElementV2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []  # stack is a decrease stack
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:  # if find cur > stack[-1], do stack.pop
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    s = Solution()
    a = s.nextGreaterElement(nums1, nums2)
    print(a)

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    a = s.nextGreaterElement(nums1, nums2)
    print(a)

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    a = s.nextGreaterElementV2(nums1, nums2)
    print(a)

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    a = s.nextGreaterElementV2(nums1, nums2)
    print(a)
