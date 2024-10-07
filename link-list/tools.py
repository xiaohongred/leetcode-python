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


def printList(head: ListNode):
    while head:
        print(head.val, end="")
        print("->", end="")
        head = head.next
    print()
