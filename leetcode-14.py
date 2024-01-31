from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        res = ""

        for i in range(min_len):
            if len(set([s[i] for s in strs])) > 1:
                break
            res += strs[0][i]
        return res


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    s = Solution()
    a = s.longestCommonPrefix(strs)
    print(a)
