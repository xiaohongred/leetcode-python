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
        return 0


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    s = Solution()
    a = s.strStr(haystack, needle)
    print(a)
