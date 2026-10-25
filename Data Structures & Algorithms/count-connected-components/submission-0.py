class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # similar to counting islands, but for connected components withiin a graph
        # dfs on each node and we will have a visited set 
        connected = {n: [] for n in range(n)}
        for n1, n2 in edges:
            connected[n1].append(n2)
            connected[n2].append(n1)
        visited = set()
        def dfs(n):
            if n in visited:
                return 
            visited.add(n)
            for nei in connected[n]:
                dfs(nei)
        out = 0
        for node in range(n):
            last = len(visited)
            dfs(node)
            if last != len(visited):
                out += 1
        return out