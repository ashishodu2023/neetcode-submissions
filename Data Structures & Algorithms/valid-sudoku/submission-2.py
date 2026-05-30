class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        seen = set()

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue 
                
                row_key = (row,value)
                col_key = (value,col)
                box_key = (row//3, col//3, value)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False 
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True
        