class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we just need to deterine if there are any cycles within this graph
        # and if every node is connected
        adjacency_list = {v: [] for v in range(n)}
        for e1, e2 in edges:
            adjacency_list[e1].append(e2)
            adjacency_list[e2].append(e1)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjacency_list[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            return True
        if not dfs(0, None):
            return False
        print(visited)
        return len(visited) == n