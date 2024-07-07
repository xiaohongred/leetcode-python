from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v, in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True

                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res


if __name__ == '__main__':
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    s = Solution()
    a = s.findItinerary(tickets)
    print(a)

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    a = s.findItinerary(tickets)
    print(a)
