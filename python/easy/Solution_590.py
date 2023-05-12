# 589. N-ary Tree Preorder Traversal

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            if node.children:
                stack += node.children
        return ans[::-1]


root = Node(1)
node3 = Node(3)
node2 = Node(2)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node3.children = [node5, node6]
root.children = [node3, node2, node4]
ans = Solution().postorder(root)
print(ans)
