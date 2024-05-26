import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:  # 如果 prev 非空，但堆已经空了
                return ""
            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            newCnt = cnt + 1

            if prev:  # 本次循环选择了字符后，时才把上一次循环使用的字符加入堆中供选择
                heapq.heappush(maxHeap, prev)
                prev = None

            if newCnt != 0:
                prev = [cnt + 1, char]

        return res


if __name__ == '__main__':
    s = "aab"
    solu = Solution()
    a = solu.reorganizeString(s)
    print(a)

    s = "aaab"
    a = solu.reorganizeString(s)
    print(a)
