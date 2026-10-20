# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            if n1.val == n2.val:
                return sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)
            else:
                return False
                
        def checkNode(n):
            if sameTree(n, subRoot):
                return True
            if n:
                return checkNode(n.left) or checkNode(n.right)
        
        if checkNode(root):
            return True
        return False