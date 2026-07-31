from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [list(col) for col in zip(*board)]
        squares = [[] for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                square_index = int((row)/3) * 3 + int((col)/3)
                if board[row][col] != ".":
                    squares[square_index].append(str(board[row][col]))

        for square in squares:
            square_count = Counter(square)
            for num in range(1,10):
                if str(num) in square_count.keys():
                    if square_count[str(num)] > 1:
                        return False


        for row in range(len(board)):
            row_count = Counter(board[row])

            for num in range(9):
                if row_count[str(num)]:
                    if row_count[str(num)] > 1:
                        return False
        
        for col in cols:
            col_count = Counter(col)
            for num in col_count.keys():
                if num == ".":
                    continue
                else:
                    if col_count[num] > 1:
                        return False

        return True
