class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        out = []
        for x, y in points:
            dist = -math.sqrt(x ** 2 + y ** 2)
            ele = (dist, x, y)
            heap.append(ele)
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        for point in heap:
            out.append([point[1], point[2]])
        return out