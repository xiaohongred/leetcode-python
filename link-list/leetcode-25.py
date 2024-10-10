# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        groupPrev = dummy  # 当前组的前一个元素
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next  # 当前组的后一个元素

            # reverse group
            prev, curr = kth.next, groupPrev.next  # curr， prev  之间的元素就是当前组
            while curr != groupNext:  # 翻转当前组
                tmp = curr.next
                curr.next = prev  # 当前组翻转前的第一个元素(翻转后的最后一个元素) 指向下一组的第一个元素
                prev = curr
                curr = tmp
            tmp = groupPrev.next  # 当前组的第一个元素， 之后会成为下一组的前一个元素
            groupPrev.next = kth
            groupPrev = tmp  # 当前组的第一个元素， 之后会成为下一组的前一个元素
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    k = 2
    head = tools.buildList(head)
    tools.printList(head)
    a = s.reverseKGroup(head, k)
    tools.printList(a)

    head = [1, 2, 3, 4, 5]
    k = 3
    head = tools.buildList(head)
    tools.printList(head)
    a = s.reverseKGroup(head, k)
    tools.printList(a)
