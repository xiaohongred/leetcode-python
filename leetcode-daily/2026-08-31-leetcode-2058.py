# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isCriticalPoint(self, prev: ListNode, curr: ListNode, next: ListNode) -> bool:
        if prev is None or next is None:
            return False
        return (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val)
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        critical_points = []
        index = 0
        prev = None
        curr = head
        next_node = head.next if head else None

        while curr:
            if self.isCriticalPoint(prev, curr, next_node):
                critical_points.append(index)
            prev = curr
            curr = next_node
            next_node = next_node.next if next_node else None
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance, max_distance]



if __name__ == "__main__":
    s = Solution()
    # Example usage:
    # Create a linked list: [3,1]
    head = ListNode(3, ListNode(1))
    print(s.nodesBetweenCriticalPoints(head))  # Output: [-1, -1]


    # head = [5,3,1,2,5,1,2]
    head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
    print(s.nodesBetweenCriticalPoints(head))  # Output: [1, 3]

    # head = [1,3,2,2,3,2,2,2,7]
    head = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))
    print(s.nodesBetweenCriticalPoints(head))