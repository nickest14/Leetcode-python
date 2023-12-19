# 203. Remove Linked List Elements

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
            self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            next = curr.next
            if curr.val == val:
                prev.next = next
            else:
                prev = curr
            curr = next


l6 = ListNode(val=5)
l5 = ListNode(val=4, next=l6)
l4 = ListNode(val=3, next=l5)
l3 = ListNode(val=9, next=l4)
l2 = ListNode(val=2, next=l3)
l1 = ListNode(val=1, next=l2)

ans = Solution().removeElements(l1, 9)
while ans:
    print(ans.val)
    ans = ans.next
