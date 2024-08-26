# 590. N-ary Tree Postorder Traversal

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val: int = val
        self.children: list[Node] = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack: list[Node] = [root]
        ans: list[int] = []
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
