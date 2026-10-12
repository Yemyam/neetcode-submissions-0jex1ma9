# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dive(node):
            if node.right == None and node.left == None:
                return 1
            elif node.right and node.left:
                return max(dive(node.right)+ 1, dive(node.left) + 1)
            elif not node.left:
                return dive(node.right) + 1
            else:
                return dive(node.left) + 1
        if not root:
            return 0
        return dive(root)
            