# 2807. Insert Greatest Common Divisors in Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x: int, y: int) -> int:
            while y != 0:
                x, y = y, x % y
            return x

        cur = head
        while cur and cur.next:
            node = ListNode(gcd(cur.val, cur.next.val))
            node.next = cur.next
            cur.next = node
            cur = node.next

        return head


values: list[int] = [18, 6, 10, 3]
head = cur = ListNode(values[0])
for i in values[1:]:
    cur.next = ListNode(i)
    cur = cur.next

ans = Solution().insertGreatestCommonDivisors(head)
print(ans)
