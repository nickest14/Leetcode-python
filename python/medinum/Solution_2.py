# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2):
            return []
        index, total_val = 0, 0
        l1_flag, l2_flag = False, False
        if l1:
            l1_flag = True
            total_val += l1.val
        if l2:
            l2_flag = True
            total_val += l2.val
        while l1_flag or l2_flag:
            index += 1
            if l1_flag:
                if l1 and l1.next:
                    l1 = l1.next
                    total_val += l1.val * 10**index
                else:
                    l1_flag = False
            if l2_flag:
                if l2 and l2.next:
                    l2 = l2.next
                    total_val += l2.val * 10**index
                else:
                    l2_flag = False
        ans = [int(i) for i in str(total_val)[::-1]]
        return ans


l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)
l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)
l2.next = l2_1
l2_1.next = l2_2
ans = Solution().addTwoNumbers(l1, l2)
print(ans)
