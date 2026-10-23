# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can do bst here and construct an array of levels, and return the last element for each level in the tree
        q = collections.deque()
        q.append(root)
        levels = []
        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft()
                if n == None:
                    continue
                level.append(n.val)
                q.append(n.left)
                q.append(n.right)
            if len(level) != 0:
                levels.append(level)
        out = []
        for level in levels:
            out.append(level[-1])
        return out

                