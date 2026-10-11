class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def island_area(r, c):
            area = 1
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r1, c1 = row + dr, col + dc
                    if r1 in range(rows) and c1 in range(cols) and grid[r1][c1] == 1 and (r1, c1) not in visited:
                        visited.add((r1, c1))
                        q.append((r1, c1))
                        area += 1
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = island_area(r, c)
                    max_area = max(area, max_area)
        return max_area