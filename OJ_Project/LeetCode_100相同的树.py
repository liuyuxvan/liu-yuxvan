# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p, q) -> int:
        n=1
        def dfs(p: TreeNode, q: TreeNode):
            if p.val == q.val:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
            else:n=0
