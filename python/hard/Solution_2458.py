# 2458. Height of Binary Tree After Subtree Removal Queries

from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth: dict[int, int] = defaultdict(int)
        height: dict[int, int] = defaultdict(int)

        def dfs(node: TreeNode, cur_depth: int):
            if not node:
                return -1
            depth[node.val] = cur_depth
            h = max(dfs(node.left, cur_depth + 1), dfs(node.right, cur_depth + 1)) + 1
            height[node.val] = h
            return h

        dfs(root, 0)

        cousins: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for val, dep in depth.items():
            cousins[dep].append((-height[val], val))
            cousins[dep].sort()
            if len(cousins[dep]) > 2:
                cousins[dep].pop()

        ans: list[int] = []
        for query in queries:
            dep: int = depth[query]
            if len(cousins[dep]) == 1:
                ans.append(dep - 1)
            else:
                ind: int = 1 if cousins[dep][0][1] == query else 0
                ans.append(-(cousins[dep][ind][0]) + dep)

        return ans


root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)
ans = Solution().treeQueries(root, [3, 2, 4, 8])
print(ans)
