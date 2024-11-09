from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def isSubseq(s, subseq):
            i1, i2 = 0, 0
            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != p[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(subseq)

        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[: m + 1])
            if isSubseq(s, p):
                l = m + 1
                res = max(res, m + 1)
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "abcacb"
    p = "ab"
    removable = [3, 1, 0]
    a = solu.maximumRemovals(s, p, removable)
    print(a)

    s = "abcbddddd"
    p = "abcd"
    removable = [3, 2, 1, 4, 5, 6]
    a = solu.maximumRemovals(s, p, removable)
    print(a)

    s = "abcab"
    p = "abc"
    removable = [0, 1, 2, 3, 4]
    a = solu.maximumRemovals(s, p, removable)
    print(a)
