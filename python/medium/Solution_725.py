# 725. Split Linked List in Parts

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length: int = 0
        current: ListNode = head
        while current:
            length += 1
            current = current.next

        base_size, extra = divmod(length, k)
        current = head
        ans: list[ListNode] = []
        for _ in range(k):
            dummy = ListNode()
            part_head = dummy
            for _ in range(base_size + (1 if extra > 0 else 0)):
                dummy.next = current
                dummy = current
                current = current.next
            if extra > 0:
                extra -= 1

            dummy.next = None
            ans.append(part_head.next)

        return ans


head = ListNode(1)
cur = head
for i in range(2, 11):
    node = ListNode(i)
    cur.next = node
    cur = node
ans = Solution().splitListToParts(head, 3)
print(ans)
