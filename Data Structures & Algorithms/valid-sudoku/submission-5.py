class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j] not in check:
                    if board[i][j] != '.':
                        check.add(board[i][j])
                else:
                    print(1, i, j)
                    return(False)
        
        for j in range(9):
            check = set()
            for i in range(9):
                if board[i][j] not in check:
                    if board[i][j] != '.':
                        check.add(board[i][j])
                else:
                    print(2, i, j)
                    return(False)
        
        for i in range(9):
            sr = 3 * (i//3)
            sc = 3 * (i%3)

            check = set()

            for j in range(3):
                for k in range(3):
                    if board[sr + j][sc + k] not in check:
                        if board[sr + j][sc + k] != '.':
                            check.add(board[sr + j][sc + k])
                    else:
                        print(3, sr + j, sc + k)
                        return(False)
        
        return(True)
        

        
        











        