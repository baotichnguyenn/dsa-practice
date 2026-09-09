# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> (bool, int):
            if root is None:
                return True, 0

            left_bal, left_height = dfs(root.left)
            right_bal, right_height = dfs(root.right)

            is_node_balanced = abs(right_height - left_height) <= 1
            if is_node_balanced and left_bal and right_bal:
                return True, max(right_height, left_height) +1
            else: 
                return False, max(right_height, left_height)+1

        balanced, height = dfs(root)
        return balanced

        