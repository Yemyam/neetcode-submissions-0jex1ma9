class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find, if we try to union two components with the same parent then that is the cycle
        n = len(edges)
        parents = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        # return the parent of a node, also path compress
        def find(node):
            out = parents[node]
            while out != parents[out]:
                parents[out] = parents[parents[out]]
                out = parents[out]
            return out
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return True
            else:
                new_rank = rank[p1] + rank[p2]
                if rank[p1] > rank[p2]:
                    parents[p2] = p1
                else:
                    parents[p1] = p2
                rank[p1] = new_rank
                rank[p2] = new_rank
                return False

        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]