class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        curNode = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curNode
        self.right.prev = curNode
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1

        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0


if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    k = 10
    obj = MyCircularQueue(k)

    value = 12
    param_1 = obj.enQueue(value)
    obj.enQueue(value)
    obj.enQueue(13)
    print(param_1)
    param_2 = obj.deQueue()
    print(param_2)
    param_3 = obj.Front()
    print(param_3)
    param_4 = obj.Rear()
    print(param_4)
    param_5 = obj.isEmpty()
    print(param_5)
    param_6 = obj.isFull()
    print(param_6)
