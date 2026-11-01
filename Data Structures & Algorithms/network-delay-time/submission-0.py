class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstras, basically just like bfs, but we use a min heap with the node and the cost, instead of just a queue
        # initalize the min heap with the starting node within it, (cost, node)
        heap = [(0, k)]
        visited = set()
        adj = {i: [] for i in range(1, n + 1)}
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        while heap:
            time, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            visited.add(curr)
            out = time
            for nei in adj[curr]:
                if nei not in visited:
                    heapq.heappush(heap, (nei[0] + time, nei[1]))
        if len(visited) != n:
            return -1
        return out

            