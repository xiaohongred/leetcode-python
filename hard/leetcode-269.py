# https://www.lintcode.com/problem/892/description
from heapq import heapify, heappop, heappush
from typing import (
    List,
)


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    # lintcode 无法通过
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        if not words:
            return ''
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        res = []
        visited = {}  # False=visited,  True=visited and current path

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
            return False

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

    def alienOrder(self, words):
        # Write your code here
        from collections import defaultdict
        from collections import deque
        import heapq

        graph = {}

        # initial graph
        for w in words:
            for c in w:
                graph[c] = set()

        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i - 1][j] != words[i][j]:
                    graph[words[i - 1][j]].add(words[i][j])
                    break

        indegree = defaultdict(int)
        for g in graph:
            for ne in graph[g]:
                indegree[ne] += 1

        q = [w for w in graph if indegree[w] == 0]
        heapq.heapify(q)

        order = []
        visited = set()
        while q:
            # n = q.pop()
            n = heapq.heappop(q)

            if n in visited:
                continue
            visited.add(n)
            order.append(n)

            for ne in graph[n]:
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    # q.appendleft(ne)
                    heapq.heappush(q, ne)
        return ''.join(order) if len(order) == len(graph) else ''


if __name__ == '__main__':
    # 还没有理解， 上面的是错误的，没有ac
    s = Solution()
    dic = ["wrt", "wrf", "er", "ett", "rftt"]
    a = s.alien_order(dic)
    print(a)

    dic = ["z", "x"]
    a = s.alien_order(dic)
    print(a)

    dic = ["ab", "adc"]
    a = s.alien_order(dic)  # 无法通过
    print(a)

    dic = ["wrt", "wrf", "er", "ett", "rftt"]
    a = s.alienOrder(dic)
    print(a)

    dic = ["z", "x"]
    a = s.alienOrder(dic)
    print(a)

    dic = ["ab", "adc"]
    a = s.alienOrder(dic)  # 可以通过
    print(a)

    dic = ["abc", "ab"]
    a = s.alienOrder(dic)  # 无法通过
    print(a)
