from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l = 0
        for r in range(len(people) - 1, -1, -1):
            if r < l:
                break
            if people[r] + people[l] <= limit:
                l += 1
            res += 1

        return res

    def numRescueBoatsV2(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0

        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res


if __name__ == '__main__':
    people = [1, 2]
    limit = 3
    s = Solution()
    a = s.numRescueBoats(people, limit)
    print(a)

    people = [3, 5, 3, 4]
    limit = 5
    a = s.numRescueBoats(people, limit)
    print(a)
