class StockSpanner:

    def __init__(self):
        self.stack = []  # pair : (price, span)      单调栈

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


if __name__ == '__main__':
    s = StockSpanner()
    a = s.next(100)
    print(a)
    a = s.next(80)
    print(a)
    a = s.next(60)
    print(a)
    a = s.next(70)
    print(a)
    a = s.next(60)
    print(a)
    a = s.next(75)
    print(a)
    a = s.next(85)
    print(a)
