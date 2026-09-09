# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)
            val  = root.val
            return left, right, val
        
        if p is None or q is None:
            return p is q

        if p.val != q.val:
            return False

        left_p, right_p, val_p = dfs(p)
        left_q, right_q, val_q = dfs(q)

        if left_p == left_q and right_p == right_q and val_p == val_q:
            return True
        else:
            return False
        