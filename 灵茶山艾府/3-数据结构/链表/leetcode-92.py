# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummyNode = ListNode(next=head)
        p0 = dummyNode
        for _ in range(left-1):
            p0 = p0.next
        
        pre = None
        cur = p0.next

        for _ in range(right - left + 1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        p0.next.next = cur  # 2 指向 5
        p0.next = pre   # 1 指向 2
        return dummyNode.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = s.reverseBetween(head, 2, 4)
    # 输出反转后的链表
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print("None")  # 输出 None 表示链表结束