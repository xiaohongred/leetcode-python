class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += (n & 0b1)
            n = n >> 1
        return count

    def hammingWeightV2(self, n: int) -> int:
        count = 0
        while (n):
            count += 1
            n = n & (n - 1)  # 每次都除去一个bit为1的位
        return count


if __name__ == '__main__':
    n = 11
    s = Solution()
    a = s.hammingWeight(n)
    print(a)

    b = s.hammingWeightV2(n)
    print(b)
