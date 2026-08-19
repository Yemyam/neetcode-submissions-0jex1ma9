# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next      # save before overwriting
            curr.next = prev     # flip the pointer
            prev = curr          # advance both
            curr = nxt
        return prev              # prev is the new head
