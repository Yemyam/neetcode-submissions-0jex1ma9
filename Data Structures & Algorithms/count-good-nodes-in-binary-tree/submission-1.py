# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.out = 0
        # we can use dfs to traverse the tree and keep track of the value of the largest ancestor node
        def dfs(node, largest):
            if not node:
                return
            if node.val >= largest:
                self.out += 1
                largest = node.val
            dfs(node.left, largest)
            dfs(node.right, largest)
        dfs(root, -float("inf"))
        return self.out