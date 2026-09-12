# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val="")
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            curr.next = ListNode()
            curr = curr.next
        while list1:
            curr.val = list1.val
            list1 = list1.next
            if list1:
                curr.next = ListNode()
            else:
                curr.next = None
            curr = curr.next
        while list2:
            curr.val = list2.val
            list2 = list2.next
            curr.next = ListNode()
            if list2:
                curr.next = ListNode()
            else:
                curr.next = None
            curr = curr.next

        return head


