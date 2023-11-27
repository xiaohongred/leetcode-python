from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        qLen = len(self.q)
        for i in range(qLen - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == '__main__':
    pass
