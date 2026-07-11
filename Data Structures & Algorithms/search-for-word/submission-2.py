class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        visited = set()
        rows = len(board)
        cols = len(board[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            for col in range(cols):

                def dfs(row, col, index):
                    if index == len(word):
                        return True

                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        return False

                    if (row, col) in visited:
                        return False

                    if board[row][col] != word[index]:
                        return False

                    visited.add((row, col))

                    for dr, dc in directions:
                        if dfs(dr + row, dc + col, index + 1):
                            return True

                    visited.remove((row, col))
                    return False

                if dfs(row, col, 0):
                    return True

        return False
