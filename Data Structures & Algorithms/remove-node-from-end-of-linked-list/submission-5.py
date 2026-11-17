# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a plain list containing the nodes
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next

        id_to_remove = len(nodes) - n
        if id_to_remove == 0:
            return head.next
        nodes[id_to_remove - 1].next = nodes[id_to_remove].next 
        return head       

