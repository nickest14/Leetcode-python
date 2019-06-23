# 21. Merge Two Sorted Lists


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        linkedlist = []
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    linkedlist.append(l1.val)
                    l1 = l1.next if l1.next else None
                else:
                    linkedlist.append(l2.val)
                    l2 = l2.next if l2.next else None
            else:
                if l1:
                    linkedlist.append(l1.val)
                    l1 = l1.next if l1.next else None
                else:
                    linkedlist.append(l2.val)
                    l2 = l2.next if l2.next else None
        return linkedlist


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


ans = Solution().mergeTwoLists(l1, l2)
print(ans)
