class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        pali = {}  # bitmask: [length, subStr]

        for mask in range(1, 1 << N):
            subSeq = ""
            for i in range(N):
                if mask & (1 << i):
                    subSeq += s[N - i - 1]
            reverseStr = subSeq[:: -1]
            if subSeq == reverseStr:
                pali[mask] = [len(subSeq), subSeq]
        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res, pali[m1][0] * pali[m2][0])
                    # print(pali[m1][1], pali[m2][1])

        return res


if __name__ == '__main__':
    s = "leetcodecom"
    solu = Solution()
    a = solu.maxProduct(s)
    print(a)
