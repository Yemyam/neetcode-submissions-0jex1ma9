# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            # first we need to check if one of the nodes does not exist
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            # both nodes exist
            if n1.val != n2.val:
                return False
            return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
        out = True
        out = dfs(p, q)
        if not out:
            return False
        return True
                
