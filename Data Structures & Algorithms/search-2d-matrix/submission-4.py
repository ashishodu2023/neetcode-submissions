class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 
        right = rows * cols - 1

        while left<=right:

            mid = (left + right) //2
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True 

            if value < target:
                left = mid + 1
            if value > target:
                right = mid -1 

        
        return False

            
        