# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # solution
        # we can determine the directions that we need to go to reach p and q 
        # when these directions diverge, thats essentially when we know that we are at the lca
        # we can start at the root node, and dfs when p and q agree, when p and q diverge, thats going to be our lca
        def dfs(n):
            if p.val > n.val and q.val > n.val:
                return dfs(n.right)
            elif p.val < n.val and q.val < n.val:
                return dfs(n.left)
            else:
                return n
        node = root
        return dfs(node)
