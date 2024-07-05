# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        critical_points = []
        prev = head
        cur = head.next
        position = 1
        while cur.next:
            if (prev.val < cur.val and cur.next.val < cur.val) or (prev.val > cur.val and cur.next.val > cur.val):
                critical_points.append(position)
            position += 1
            prev = cur
            cur = cur.next

        if len(critical_points) < 2:
            return [-1, -1]

        max_distance = critical_points[-1] - critical_points[0]
        min_distance = max_distance
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance, max_distance]


head = cur = ListNode(5)
for i in [3, 1, 2, 5, 1, 2]:
    node = ListNode(i)
    cur.next = node
    cur = cur.next

ans = Solution().nodesBetweenCriticalPoints(head)
print(ans)
