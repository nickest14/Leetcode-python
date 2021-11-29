# 160. Intersection of Two Linked Lists


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            nodeA = headB if not nodeA else nodeA.next
            nodeB = headA if not nodeB else nodeB.next
        return nodeA


intersection_node = ListNode(2)
intersection_node.next = ListNode(4)

headA = ListNode(9)
headA.next = ListNode(1)
headA.next.next = intersection_node

headB = ListNode(3)
headB.next = intersection_node

ans = Solution().getIntersectionNode(headA, headB)
print(ans)
