class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        target_row = None
        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                target_row = middle
                break
            elif matrix[middle][0] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
        if target_row is None:
            return False
        left = 0
        right = len(matrix[target_row]) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[target_row][middle] == target:
                return True
            elif matrix[target_row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False