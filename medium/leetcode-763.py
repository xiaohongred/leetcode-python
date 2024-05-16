from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # char -> last index in s
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastIndex[c] > end:
                end = lastIndex[c]
            if i == end:
                res.append(size)
                size = 0
        return res


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    solu = Solution()
    a = solu.partitionLabels(s)
    print(a)
