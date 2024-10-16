class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildList(arr: list[int]) -> ListNode:
    dummyHead = ListNode()
    p = dummyHead
    for n in arr:
        p.next = ListNode(n)
        p = p.next
    return dummyHead.next


def buildCircleList(arr: list[int], i: int) -> ListNode:
    dummyHead = ListNode()
    p = dummyHead
    indexToNodeMap = {}
    curIndex = 0
    for n in arr:
        p.next = ListNode(n)
        indexToNodeMap[i] = p.next
        p = p.next
    if i >= 0:
        p.next = indexToNodeMap[i]
    return dummyHead.next


def printList(head: ListNode):
    while head:
        print(head.val, end="")
        print("->", end="")
        head = head.next
    print()
