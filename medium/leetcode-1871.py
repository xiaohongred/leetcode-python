from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q, farthest = deque([0]), 0
        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        return False


if __name__ == '__main__':
    s = "011010"
    minJump = 2
    maxJump = 3

    solu = Solution()
    a = solu.canReach(s, minJump, maxJump)
    print(a)

    s = "01101110"
    minJump = 2
    maxJump = 3
    a = solu.canReach(s, minJump, maxJump)
    print(a)
