# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reverse the linked list, then step through the
        curr = head
        nodes = {}
        i = 0
        while curr:
            nodes[i] = curr
            curr = curr.next
            i += 1
        n = len(nodes.keys()) - 1
        i = 0
        dummy = ListNode() 
        curr = dummy
        alternate = True
        while i <= n:
            if alternate:
                curr.next = nodes[i]
                i += 1
            else:
                curr.next = nodes[n]
                n -= 1
            curr = curr.next
            alternate = not alternate
        curr.next = None
        