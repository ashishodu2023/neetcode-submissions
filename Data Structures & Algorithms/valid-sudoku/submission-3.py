class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if not board:
            return []
        
        seen = set()

        for i in range(9):
            for j in range(9):

                value = board[i][j]

                if value == ".":
                    continue
                
                row_id = f"row{i}{value}"
                col_id = f"col{j}{value}"
                box_id = f"box{i//3}{j//3}{value}"

                if row_id in seen or col_id in seen or box_id in seen:
                    return False
                
                seen.add(row_id)
                seen.add(col_id)
                seen.add(box_id)
        
        return True