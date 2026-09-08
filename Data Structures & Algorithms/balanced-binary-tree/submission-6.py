# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root):
        if not root:
            return 0

        left = self.check(root.left)
        if left == -1:
            return -1

        right = self.check(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root):
        return self.check(root) != -1
        