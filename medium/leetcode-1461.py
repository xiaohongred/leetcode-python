class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        kHash = set()
        for i in range(len(s) - k + 1):
            kHash.add(s[i:i + k])
        return len(kHash) == 2 ** k


if __name__ == '__main__':
    s = "00110110"
    k = 2
    solu = Solution()
    a = solu.hasAllCodes(s, k)
    print(a)

    s = "0110"
    k = 1
    a = solu.hasAllCodes(s, k)
    print(a)

    s = "0110"
    k = 2
    a = solu.hasAllCodes(s, k)
    print(a)
