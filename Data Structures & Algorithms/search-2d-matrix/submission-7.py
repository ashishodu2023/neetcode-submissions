class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            row_value = mid // cols
            col_value = mid % cols

            value = matrix[row_value][col_value]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            elif value > target:
                right = mid - 1

        return False
