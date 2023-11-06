# 61. Rotate List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        old_head = head

        node, size = head, 0
        while node:
            node, size = node.next, size + 1

        if k % size == 0:
            return head

        k %= size
        slow = fast = head
        while fast and fast.next:
            if k <= 0:
                slow = slow.next
            fast = fast.next
            k -= 1

        new_tail, new_head, old_tail = slow, slow.next, fast
        new_tail.next, old_tail.next = None, old_head

        return new_head


haed = ListNode(1)
haed.next = ListNode(2)
haed.next.next = ListNode(3)
haed.next.next.next = ListNode(4)
haed.next.next.next.next = ListNode(5)
Solution().rotateRight(haed, 2)
