class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permS1 = []
        used = [False] * len(s1)

        def backtrack(path: str, used: list[int]):
            if len(path) == len(s1):
                permS1.append(path)
                return
            for i in range(len(s1)):
                if not used[i]:
                    used[i] = True
                    backtrack(path + s1[i], used)
                    used[i] = False
            return

        backtrack("", used)

        for p in permS1:
            if p in s2:
                return True
        return False

    def checkInclusionV2(self, s1: str, s2: str) -> bool:
        s1Map = {}  # char -> int
        s2WindowMap = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1Map[s1[i]] = s1Map.get(s1[i], 0) + 1
            s2WindowMap[s2[i]] = s2WindowMap.get(s2[i], 0) + 1

        if s1Map == s2WindowMap:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            s2WindowMap[s2[l]] = s2WindowMap.get(s2[l], 0) - 1
            if s2WindowMap[s2[l]] == 0:
                s2WindowMap.pop(s2[l])
            s2WindowMap[s2[r]] = s2WindowMap.get(s2[r], 0) + 1
            if s2WindowMap == s1Map:
                return True
            r += 1
            l += 1
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()
    a = s.checkInclusionV2(s1, s2)
    print(a)

    s1 = "ab"
    s2 = "eidboaoo"
    a = s.checkInclusionV2(s1, s2)
    print(a)

    s1 = "a"
    s2 = "ab"
    a = s.checkInclusionV2(s1, s2)
    print(a)

    s1 = "adc"
    s2 = "dcda"
    a = s.checkInclusionV2(s1, s2)
    print(a)
