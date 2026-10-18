class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each treasure chest in a multiple source bfs and update each land tile with its distance from the nearest treasure
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = 0

        for r in range(rows):
            for c in range(cols):
                # add each treasure chest into a queue
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        while q:
            dist += 1
            for item in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    # check if cell is in bounds and if cell has not been visited yet
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                        # check if cell is land
                        if grid[nr][nc] == 2147483647:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            grid[nr][nc] = dist
    



