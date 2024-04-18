from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        listLen = 1
        tail = head
        while tail.next:
            listLen += 1
            tail = tail.next

        realK = (k % listLen)
        if realK == 0:
            return head

        pivotIndex = listLen - realK - 1
        cur = head
        for _ in range(pivotIndex):  # 移动到新的头结点的前一个节点
            cur = cur.next
        newHead = cur.next  # 新的头结点
        cur.next = None  # 新的尾节点指向None
        tail.next = head  # 原来的尾节点指向原来的头节点
        return newHead


if __name__ == '__main__':
    pass
