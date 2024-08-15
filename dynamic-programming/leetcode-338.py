from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:  # offset: 1, 2, 4, 8, 16 ...
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

    ###
    # 0    0000
    # 1    0001          offset = 1
    # 2    0010
    # 3    0011          offset = 2
    # 4    0100          offset = 4
    # 5    0101
    # 6    0110
    # 7    0111
    # 8    1000          offset = 8        dp[i] = 1 + dp[i - offset]

    ###


if __name__ == '__main__':
    n = 2
    s = Solution()
    a = s.countBits(n)
    print(a)

    n = 20
    a = s.countBits(n)
    print(a)
