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

                row_id = f"row_id{row}{value}"
                col_id = f"col_id{col}{value}"
                box_id = f"box_id{row // 3}{col // 3}{value}"

                if row_id in seen or col_id in seen or box_id in seen:
                    return False

                seen.add(row_id)
                seen.add(col_id)
                seen.add(box_id)

        return True
