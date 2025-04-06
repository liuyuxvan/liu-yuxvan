# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if  not root:
            return
        if root.left:
            temp=TreeNode(-1)
            temp.left=root.left
            root.left=temp
            self.expandBinaryTree(root.left.left)
        if root.right:
            temp=TreeNode(-1)
            temp.right=root.right
            root.right=temp
            self.expandBinaryTree(root.right.right)
        return root

