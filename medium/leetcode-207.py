from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        print(preMap)
        visitSet = set()

        def dfs(crs):
            print(preMap)
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    s = Solution()
    a = s.canFinish(numCourses, prerequisites)
    print(a)
