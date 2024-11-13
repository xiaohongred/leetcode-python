from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        total = len(A) + len(B)

        half = total // 2

        if len(B) < len(A):  # A 短， B 长
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # for A
            j = half - i - 2  # for B
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:  # 为什么满足这个条件就找到中点位置了
                # 因为 len(A[0:i+1])  + len(B[0:j+1])  ==  half
                # 如果满足上面的if 条件，
                #       当 total 为奇数时，中位数为  min(Aright, Bright)
                #       当 total 为偶数时，中位数是中间两个数的平均值  (max(Aleft, Bleft) + min(Aright, Bright)) / 2

                # odd
                if total % 2:
                    return min(Aright, Bright)
                else:  # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    a = s.findMedianSortedArrays(nums1, nums2)
    print(a)

    nums1 = [1, 2]
    nums2 = [3, 4]
    a = s.findMedianSortedArrays(nums1, nums2)
    print(a)
