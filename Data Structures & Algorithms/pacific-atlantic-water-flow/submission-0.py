class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # all cells that can flow into the pacific or atlantic
        pacific = []
        atlantic = []
        p_set = set()
        a_set = set()
        q = collections.deque()
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # update the pacific and atlantic arrays and queue all the adjacent cells for bfs
        for r in range(rows):
            for c in range(cols):
                # adjacent to the pacific
                if r == 0 or c == 0:
                    pacific.append((r, c))
                    p_set.add((r, c))
                # adjacent to the atlantic
                if r == (rows - 1) or c == (cols - 1):
                    atlantic.append((r, c))
                    a_set.add((r, c))

        def bfs(ocean, ocean_set):
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                        # water can only flow from a height equal to or from a height greater than
                        if heights[r][c] <= heights[nr][nc]:
                            # append the cell to ocean, since it can flow to that ocean
                            ocean.append((nr, nc))
                            ocean_set.add((nr, nc))
                            visited.add((nr, nc))
                            q.append((nr, nc))
        
        # do bfs for all pacific cells first, then for all atlantic cells
        for r, c in pacific:
            q.append((r, c))
            visited.add((r, c))

        bfs(pacific, p_set)
        q.clear()
        visited.clear()

        for r, c in atlantic:
            q.append((r, c))
            visited.add((r, c))
        
        bfs(atlantic, a_set)

        out = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in a_set and (r, c) in p_set:
                    out.append([r, c])
        return out



