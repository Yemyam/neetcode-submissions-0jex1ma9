# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we can use a min heap to store the current min head that we want to append to the list
        min_heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(min_heap)
        dummy = ListNode()
        curr = dummy
        while min_heap:
            curr_val, i, curr_node = heapq.heappop(min_heap)
            if len(min_heap) == 0:
                curr.next = curr_node
                break
            curr.next = curr_node
            curr_node = curr_node.next
            if curr_node is not None:
                heapq.heappush(min_heap, (curr_node.val, i, curr_node))
            curr = curr.next
        return dummy.next
