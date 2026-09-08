# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if not root:
            return True

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        current_balanced = (
            abs(self.height(root.left) - self.height(root.right)) <= 1
        )

        return left_balanced and right_balanced and current_balanced
        