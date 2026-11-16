class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we can start dfs from each instance of the first letter of our word on the board
        def dfs(r, c, i, visited):
            visited.add((r, c))
            if i == len(word):
                return True
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and board[nr][nc] == word[i]:
                    if dfs(nr, nc, i + 1, visited):
                        return True
            visited.remove((r, c))
            return False

        rows, cols = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, 1, visited):
                        return True
        return False