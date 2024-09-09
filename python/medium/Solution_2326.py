# 2326. Spiral Matrix IV

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans: list[list[int]] = [[-1] * n for _ in range(m)]
        ans[0][0] = head.val
        head = head.next
        r, c = 0, 0
        dr, dc = 0, 1
        while head:
            if 0 <= r + dr < m and 0 <= c + dc < n and ans[r + dr][c + dc] == -1:
                r += dr
                c += dc
                ans[r][c] = head.val
                head = head.next
            else:
                dr, dc = dc, -dr
        return ans


values: list[int] = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
head = cur = ListNode(values[0])
for i in values[1:]:
    node = ListNode(i)
    cur.next = node
    cur = cur.next

ans = Solution().spiralMatrix(3, 5, head)
print(ans)
