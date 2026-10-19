class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we can use a max heap and pop the two top elements
        # then smash the two elemnts and update the heap if nessesary 
        # finally we return the last value left in the heap
    
        # in order to use a max heap with heapq we need to invert each value
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while heap:
            # if the length of the heap is 1 just return the last element negated
            if len(heap) == 1:
                return -heap[0]
            # otherwise pop the top two elements of the heap and smash them together
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                new_stone = abs(x - y)
                heapq.heappush(heap, -new_stone)
        return 0
            


