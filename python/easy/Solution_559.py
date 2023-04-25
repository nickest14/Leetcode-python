# 559. Maximum Depth of N-ary Tree

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        return max(self.maxDepth(node) for node in root.children) + 1


node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)
node1 = Node(1, [node3, node2, node4])

ans = Solution().maxDepth(node1)
print(ans)
