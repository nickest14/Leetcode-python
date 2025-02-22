# 1028. Recover a Tree From Preorder Traversal

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None

        n: int = len(traversal)
        i: int = 0
        infos: list[tuple[int]] = []  # (val, depth)

        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1

            num_start = i
            while i < n and traversal[i].isdigit():
                i += 1

            infos.append((int(traversal[num_start:i]), depth))

        root = TreeNode(infos[0][0])
        stack: list[tuple[int]] = [
            (root, 0),
        ]
        for i in range(1, len(infos)):
            val, depth = infos[i]
            while stack and stack[-1][1] >= depth:
                stack.pop()

            parent, _ = stack[-1]
            node = TreeNode(val)

            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            stack.append([node, depth])

        return root


ans = Solution().recoverFromPreorder("1-2--3--4-5--6--7")
stack = [ans]
while stack:
    node = stack.pop(0)
    print(node.val)

    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)
    
    
    

