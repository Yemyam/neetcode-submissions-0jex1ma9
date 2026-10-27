class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we can construct the graph, and then traverse it with dfs to see if there is a cycle
        adjacency_list = {i: [] for i in range(n)}
        visited = set()
        for n1, n2 in edges:
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)
        
        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            for nei in adjacency_list[n]:
                if nei != prev:
                    if not dfs(nei, n):
                        return False
            return True
        if not dfs(0, None):
            return False
        if len(visited) != n:
            return False
        return True