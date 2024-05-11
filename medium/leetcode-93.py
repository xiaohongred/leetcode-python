from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 256 choices for each of the 4 spots but
        # The order of s stays same
        # we just place the "." in between
        res = []
        if len(s) > 12:
            return res

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) <= 255 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIP + s[i:j + 1] + ".")

        backtrack(0, 0, "")
        return res


if __name__ == '__main__':
    s = "25525511135"
    solu = Solution()
    a = solu.restoreIpAddresses(s)
    print(a)
