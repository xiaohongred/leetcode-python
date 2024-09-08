import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())  # 把队列中的前面n-1个都出对，并添加到最后
        return self.q.popleft()  # 之前在最后的元素就在最前面了，出队即可

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    obj = MyStack()
    x = 12
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
