class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # solve with union find
        # we can keep an array where each value corresponds to the parent of the node correlated with the index
        parents = [i for i in range(n)]
        rank = [1] * n
        self.out = n
        # find the parent of a node
        def find(node):
            out = node
            while node != parents[node]:
                node = parents[node]
            return node
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            # if parents are different union the nodes
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parents[p2] = p1
                else:
                    parents[p1] = p2
                rank[p1] = rank[p1] + rank[p2]
                rank[p2] = rank[p1] + rank[p2]
                self.out -= 1
        for n1, n2 in edges:
            union(n1, n2)
        return self.out
