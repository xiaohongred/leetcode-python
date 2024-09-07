from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # 正表示向右移动，负表示向左移动
            while stack and a < 0 and stack[-1] > 0:  # 只有当前小行星运动方向向左，前一个向右时，才会相撞
                diff = a + stack[-1]  # 两个小行星相撞，比较大小，看是哪个会爆炸
                if diff < 0:  # 向左移的小行星质量更大，所以前一个小行星爆炸
                    stack.pop()  # 前一个小行星爆炸
                elif diff > 0:  # 向右移动的小行星质量更大，所以当前正在向左移动的小行星爆炸
                    a = 0
                else:  # diff==0 两个小行星质量一样，都爆炸
                    a = 0
                    stack.pop()
            if a != 0:  # 在while条件中，如果 a 负的很多，把stack 中所有向右移动的小行星都撞完了，当前向左移动的a就需要入栈
                stack.append(a)
        return stack


if __name__ == '__main__':
    asteroids = [5, 10, -5]
    s = Solution()
    a = s.asteroidCollision(asteroids)
    print(a)

    asteroids = [8, -8]
    a = s.asteroidCollision(asteroids)
    print(a)

    asteroids = [10, 2, -5]
    a = s.asteroidCollision(asteroids)
    print(a)
