# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import Optional, List


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        if not root:
            return []
        if root.left:
            order.extend(self.postorderTraversal(root.left))
        else:
            order.extend(self.postorderTraversal(root.right))
        order.append(root.val)
        return order