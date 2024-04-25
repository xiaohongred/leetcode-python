from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):  # 循环 k + 1 次
            tmpprice = prices.copy()  # 使用 tmpprice 是因为每次循环，只跟新可达的节点

            # 每次循环，迭代每个航线
            for s, d, p in flights:  # s= source, d=destination, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpprice[d]:
                    tmpprice[d] = prices[s] + p
            prices = tmpprice
        return -1 if prices[dst] == float("inf") else prices[dst]


if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    s = Solution()
    a = s.findCheapestPrice(n, edges, src, dst, k)
    print(a)
