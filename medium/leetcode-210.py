from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return output


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    s = Solution()
    a = s.findOrder(numCourses, prerequisites)
    print(a)
