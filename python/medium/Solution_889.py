# 889. Construct Binary Tree from Preorder and Postorder Traversal


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        # preorder = root, left, right
        # postorder = left, right, root
        
        def make_tree() -> TreeNode:
            node  = TreeNode(postorder.pop())

            if node.val != preorder[-1]:  # post = [left, right], pre = [root, left, right]
                 node.right = make_tree()

            if node.val != preorder[-1]:  # post = [left], pre = [root, left]
                node.left = make_tree()
            
            preorder.pop()  # post = [], pre = [root], root already used for node.val

            return node

        return make_tree()


ans = Solution().constructFromPrePost([1, 2, 3], [2, 3, 1])
# ans = Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
print(ans)
