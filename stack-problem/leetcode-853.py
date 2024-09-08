from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        psPair = []
        for p, s in zip(position, speed):
            psPair.append((p, s))

        psPair.sort()

        stack = []
        for p, s in psPair[::-1]:
            t = (target - p) / s  # 在位置为p的车，以速度s跑，到达终点的时间 t
            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # 位置在前面的车到终点的时间比位置在后面的车到重点的时间更长，代表后车会与前车组成一个车队
                # 前车到终点的时间stack[-2]， 后车到终点的时间stack[-1]
                stack.pop()
        return len(stack)


if __name__ == '__main__':
    s = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    a = s.carFleet(target, position, speed)
    print(a)

    target = 10
    position = [3]
    speed = [3]
    a = s.carFleet(target, position, speed)
    print(a)

    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    a = s.carFleet(target, position, speed)
    print(a)
