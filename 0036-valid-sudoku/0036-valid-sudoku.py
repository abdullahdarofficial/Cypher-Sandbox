class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 9x9

        def checkSubMatrix(a,b):
            print(a,b)
            checkSet = set()
            for i in range(a, a + 3):
                for j in range(b , b + 3):
                    print(board[i][j], checkSet)
                    if board[i][j].isnumeric() and board[i][j] in checkSet:
                        return False
                    if board[i][j].isnumeric():
                        checkSet.add(board[i][j])
            return True


        for i in range(len(board)):
            checkRow = set()
            checkCol = set()
            for j in range(len(board[0])):
                if i % 3 == 0 and j % 3 == 0:
                    if not checkSubMatrix(i,j):
                        return False

                if board[i][j].isnumeric() and board[i][j] in checkRow:
                    return False
                if board[i][j].isnumeric():
                    checkRow.add(board[i][j])

                if board[j][i].isnumeric() and board[j][i] in checkCol:
                    return False
                if board[j][i].isnumeric():
                    checkCol.add(board[j][i])
        return True


