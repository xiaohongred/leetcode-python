from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        diff = []
        for i, c in enumerate(costs):
            diff.append((c[1] - c[0], i))  # [到B城市比到A城市多花的钱， 第i个人]

        res = 0
        diff.sort()  # 从小到大排序
        for i in range(n):
            peopleIndex = diff[i][1]
            res += costs[peopleIndex][1]  # 对于 到B城市比到A城市多花的钱 相对来说比较少的人，应该让其去B城市

        for i in range(n, 2 * n):
            peopleIndex = diff[i][1]
            res += costs[peopleIndex][0]  # 对于 到B城市比到A城市多花的钱 相对来说比较多的人，应该让其去A城市
        return res


if __name__ == '__main__':
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    s = Solution()
    a = s.twoCitySchedCost(costs)
    print(a)
