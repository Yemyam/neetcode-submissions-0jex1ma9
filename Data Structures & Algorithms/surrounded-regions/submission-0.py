class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # we can bfs search from each of the O cells on the edge of the board adding each O cell we find to an array, adding each of the coordinates of O cells into a set, then we can iterate through the array and flip all O cells that are not in that set to X's
        rows, cols = len(board), len(board[0])
        edge_o = []
        visited = set()
        q = collections.deque()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        not_captured = set()

        for r in range(rows):
            for c in range(cols):
                # check if 0 cell is on the edge of the board
                if board[r][c] == "O" and (r, c) not in visited:
                    if r == 0 or c == 0 or r == (rows - 1) or c == (cols - 1):
                        edge_o.append((r, c))
                        visited.add((r, c))
                        not_captured.add((r, c))
        
        def bfs():
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        not_captured.add((nr, nc))

        for r, c in edge_o:
            q.append((r, c))
            bfs()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in not_captured:
                    board[r][c] = "X"