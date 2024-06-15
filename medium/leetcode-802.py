from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res


if __name__ == '__main__':
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    s = Solution()
    a = s.eventualSafeNodes(graph)
    print(a)
