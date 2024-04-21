from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        n = len(gas)
        for g, c in zip(gas, cost):
            diff.append(g - c)
        if sum(diff) < 0:
            return -1
        for i in range(len(gas)):
            if diff[i] < 0:
                continue
            total = 0
            for j in range(i, i + n):
                realJ = j % n
                total += diff[realJ]
                if total < 0:
                    break
            if total >= 0:
                return i
        return -1

    def canCompleteCircuitV2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        total = 0
        start = 0
        for i in range(n):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()
    a = s.canCompleteCircuit(gas, cost)
    print(a)
