from typing import List
from collections import Counter


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):  # 返回值代表,arr[i:] 中，含有不同字母 的 子序列字符串 组成的字符串s的最大长度
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))

        return backtrack(0)


if __name__ == '__main__':
    arr = ["un", "iq", "ue"]
    s = Solution()
    a = s.maxLength(arr)
    print(a)
