"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first pass go through the array and create a hashmap with the original node 
        # as the key, and the deep copy as the value
        # then pass through the copies of nodes and update each next and random to point
        # to the deep copy of the node

        if not head:
            return None
        nodes = {}
        node = head
        while node:
            nodes[node] = Node(node.val, node.next, node.random)
            node = node.next
        
        new_head = nodes[head]
        node = new_head
        
        while node:
            if node.random:
                node.random = nodes[node.random]
            else:
                node.random = None
            if node.next:
                node.next = nodes[node.next]
            node = node.next

        return new_head
