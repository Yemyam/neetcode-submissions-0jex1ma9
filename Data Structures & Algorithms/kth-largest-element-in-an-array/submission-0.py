class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force method
        # sort the array then count k from the top
        # complexity: sorting nlogn, pass: n
        # first k elements of the array and add them to a min heap
        heap = nums[0: k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]