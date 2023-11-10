from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        k = n + m - 1

        l1 = m - 1
        l2 = n - 1

        while (l1 >= 0 and l2 >= 0):
            if nums1[l1] > nums2[l2]:

                nums1[k] = nums1[l1]
                l1 -= 1
            else:
                nums1[k] = nums2[l2]
                l2 -= 1

            k -= 1

        while (l1 >= 0):
            nums1[k] = nums1[l1]
            l1 -= 1
            k -= 1

        while (l2 >= 0):
            nums1[k] = nums2[l2]
            l2 -= 1
            k -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
