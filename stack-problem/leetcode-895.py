class FreqStack:

    def __init__(self):
        self.cnt = {}  # val -> feq
        self.maxCnt = 0  # 当前stack中，出现次数最多数对应的次数
        self.stack = {}  # freq -> list of val has this freq

    def push(self, val: int) -> None:
        valCnt = self.cnt.get(val, 0) + 1
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:  # 出现了新的最大次数
            self.maxCnt = valCnt
            self.stack[valCnt] = []  # 新的最大次数，对应的数存在 self.stack[valCnt] 列表中
        self.stack[valCnt].append(val)  # 出现最大次数valCnt，对应的数val存在 self.stack[valCnt] append进入列表

    def pop(self) -> int:
        res = self.stack[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxCnt]:  # 如果 self.stack[self.maxCnt] 为空, 将 maxCnt -= 1
            self.maxCnt -= 1
        return res

    #  5 4 5 3 4 2 5
    #  count  |   group
    #    1    | [5,4,3,2]
    #    2    | [5,4,5]
    #    3    | [5 ]


if __name__ == '__main__':
    obj = FreqStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(1)
    obj.push(2)
    obj.push(3)

    a = obj.pop()
    print(a)

    a = obj.pop()
    print(a)

    a = obj.pop()
    print(a)
