class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26

    def checkInclusionV2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map = {}  # char -> int
        s2WindowMap = {}
        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
            s2WindowMap[s2[i]] = 1 + s2WindowMap.get(s2[i], 0)

        if s1Map == s2WindowMap:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            s2WindowMap[s2[l]] = s2WindowMap.get(s2[l], 0) - 1
            if s2WindowMap[s2[l]] == 0:
                s2WindowMap.pop(s2[l])
            s2WindowMap[s2[r]] = 1 + s2WindowMap.get(s2[r], 0)
            if s2WindowMap == s1Map:
                return True
            r += 1
            l += 1
        return False


if __name__ == '__main__':
    s = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    a = s.checkInclusion(s1, s2)
    print(a)

    s1 = "ab"
    s2 = "eidboaoo"
    a = s.checkInclusion(s1, s2)
    print(a)
