# Definition for singly-linked list.
from typing import List, Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergeList.append(self.mergeList(l1, l2))

            lists = mergeList
            
        return lists[0]

    def mergeList(self, list1, list2):
        # todo
        dummyHead = ListNode()
        tail = dummyHead

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummyHead.next


if __name__ == '__main__':
    s = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    heads = []
    for l in lists:
        heads.append(tools.buildList(l))
    a = s.mergeKLists(heads)
    tools.printList(a)

    lists = []
    heads = []
    for l in lists:
        heads.append(tools.buildList(l))
    a = s.mergeKLists(heads)
    tools.printList(a)

    lists = [[]]
    heads = []
    for l in lists:
        heads.append(tools.buildList(l))
    a = s.mergeKLists(heads)
    tools.printList(a)
