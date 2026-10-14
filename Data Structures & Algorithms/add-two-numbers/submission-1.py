# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through both linked lists and create each number
        curr1 = l1
        curr2 = l2
        num1 = []
        num2 = []
        while curr1:
            num1.append(str(curr1.val))
            curr1 = curr1.next

        while curr2:
            num2.append(str(curr2.val))
            curr2 = curr2.next
    
        num1 = "".join(num1[::-1])
        num2 = "".join(num2[::-1])
        s = str(int(num1) + int(num2))
        dummy = ListNode()
        node = dummy
        for c in s[::-1]:
            node.next = ListNode(int(c))
            node = node.next
        return dummy.next