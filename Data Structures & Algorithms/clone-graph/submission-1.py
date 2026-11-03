"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we can run dfs on the graph, and use a dictionary for mapping the old nodes to the new ones
        if not node:
            return node
        old_to_new = {}
        def dfs(node):
            new_node = Node(node.val, [])
            old_to_new[node] = new_node
            for nei in node.neighbors:
                if nei not in old_to_new:
                    dfs(nei)
                old_to_new[node].neighbors.append(old_to_new[nei])
        dfs(node)
        return old_to_new[node]

        
        