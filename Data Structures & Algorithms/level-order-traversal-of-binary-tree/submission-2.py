# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        out = []
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
                out.append(level)
        return out

