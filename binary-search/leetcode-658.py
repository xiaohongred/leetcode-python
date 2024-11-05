from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2  # l, r 之间找一个窗口的起点，使得 arr[l:l+k] 最靠近x
            if x - arr[m] > arr[m + k] - x:  # arr[m]是窗口的第一个元素， arr[m+k] 是窗口外的第一个元素, 这个判断语句决定是否丢弃第一个元素 arr[m], 将窗口右移
                # 如果  x - arr[m] > arr[m + k] - x  为真，窗口右移
                l = m + 1
            else:
                r = m
        return arr[l:l + k]


if __name__ == '__main__':
    s = Solution()

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    a = s.findClosestElements(arr, k, x)
    print(a)

    arr = [1, 1, 2, 3, 4, 5]
    k = 4
    x = -1
    a = s.findClosestElements(arr, k, x)
    print(a)
