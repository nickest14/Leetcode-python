# 141. Linked List Cycle

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


node = ListNode(1)
node.next = node2 = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = node4 = ListNode(4)

node4.next = node2

ans = Solution().hasCycle(node)
print(ans)
