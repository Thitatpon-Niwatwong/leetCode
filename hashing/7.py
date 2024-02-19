class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                        board[i][j] in subgrids[i // 3][j // 3]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                subgrids[i // 3][j // 3].add(board[i][j])

        return True


A = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(A.isValidSudoku(board))
