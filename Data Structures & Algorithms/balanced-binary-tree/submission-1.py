# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # do dfs and compare sub tree heights at each level
        self.out = True
        def dfs(node):
            if not node:
                return -1
            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            if abs(l - r) > 1:
                self.out = False
            return max(l, r)
        
        dfs(root)
        return self.out