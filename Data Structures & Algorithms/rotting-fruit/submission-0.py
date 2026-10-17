import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # queue for bfs 
        q = collections.deque()
        # set for visited oranges
        visited = set()
        fresh = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # we want to bfs from all rotting oranges at the same time
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    # at the end we want to check if any fresh oranges remain
                    fresh += 1
        
        while q:
            new_rotten = False
            for rotten_orange in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
                        new_rotten = True
                        fresh -= 1
            if new_rotten:
                mins += 1 
        
        if fresh > 0:
            return -1
        return mins