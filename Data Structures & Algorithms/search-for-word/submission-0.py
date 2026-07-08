class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        visited = set()
        direction = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, 1),  # left
            (0, -1),  # right
        ]

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):

                def dfs(row, col, index):
                    # Found whole word
                    if index == len(word):
                        return True
                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        return False
                    # Wrong character
                    if board[row][col] != word[index]:
                        return False
                    # Already used
                    if (row, col) in visited:
                        return False

                    visited.add((row, col))

                    for dr, dc in direction:
                        if dfs(row + dr, col + dc, index + 1):
                            return True

                    visited.remove((row, col))
                    return False

                if dfs(row,col,0):
                    return True

        return False
