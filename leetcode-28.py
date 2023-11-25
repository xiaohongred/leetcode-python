class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            tmpRes = True
            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    tmpRes = False
                    break

            if tmpRes:
                return i

        return -1

    def strStrV2(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        needleLen = len(needle)
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i: i + needleLen] == needle:
                return i

        return -1

    def strStrKMP(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        # lps数组每个元素lps[i]表示模式字符串P从索引i开始的最长前缀,也即P[0..i-1]与P[i..P.length()-1]最长相同部分的长度。
        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]

        print(lps)  # 需要看看lps数组的定义

        i = 0  # ptr for haystack
        j = 0  # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return 0


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "adbut"
    s = Solution()
    a = s.strStrKMP(haystack, needle)
    print(a)
