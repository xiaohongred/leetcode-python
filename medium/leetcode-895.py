class FreqStack:

    def __init__(self):
        self.cnt = {}  # val -> feq
        self.maxCnt = 0  # 当前列表中出现次数最多的数字所出现的次数
        self.stack = {}  # freq -> list of val has this freq

    def push(self, val: int) -> None:
        valCnt = self.cnt.get(val, 0) + 1
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stack[valCnt] = []
        self.stack[valCnt].append(val)

    def pop(self) -> int:
        res = self.stack[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5)  # 堆栈为 [5]
    freqStack.push(7)  # 堆栈是 [5,7]
    freqStack.push(5)  # 堆栈是 [5,7,5]
    freqStack.push(7)  # 堆栈是 [5,7,5,7]
    freqStack.push(4)  # 堆栈是 [5,7,5,7,4]
    freqStack.push(5)  # 堆栈是 [5,7,5,7,4,5]
    print(freqStack.pop())  # 返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
    print(freqStack.pop())  # 返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
    print(freqStack.pop())  # 返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
    print(freqStack.pop())  # 返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
