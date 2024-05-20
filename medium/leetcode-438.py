from collections import defaultdict
from typing import List


class Solution:
    def dicts_are_equal(self, defaultdict1, defaultdict2):
        return dict(defaultdict1) == dict(defaultdict2)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = defaultdict(int)
        window = defaultdict(int)
        for c in p:
            need[c] += 1
        left, right = 0, 0
        res = []
        while right < len(s):
            c = s[right]
            window[c] += 1

            if right - left == len(p) - 1:
                if self.dicts_are_equal(need, window):
                    res.append(left)

                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            right += 1
        return res

    def findAnagramsV2(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"

    solu = Solution()
    a = solu.findAnagrams(s, p)
    print(a)

    s = "abab"
    p = "ab"
    a = solu.findAnagrams(s, p)
    print(a)
