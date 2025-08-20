class Solution(object):
    def isValidSudoku(self, board):
        
        for i in range(9):
            dict_row = {}
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in dict_row:
                        return False
                    else:
                        dict_row[board[i][j]] = i
        
        for i in range(9):
            dict_col = {}
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in dict_col:
                        return False
                    else:
                        dict_col[board[j][i]] = i

        dict_1 = {}
        dict_2 = {}
        dict_3 = {}
        for i in range(9):
            if i % 3 == 0:
                dict_1 = {}
                dict_2 = {}
                dict_3 = {}
            for j in range(9):
                if board[i][j] != ".":
                    if j < 3:
                        if board[i][j] in dict_1:
                            return False
                        else:
                            dict_1[board[i][j]] = i
                    elif j < 6:
                        if board[i][j] in dict_2:
                            return False
                        else:
                            dict_2[board[i][j]] = i
                    else:
                        if board[i][j] in dict_3:
                            return False
                        else:
                            dict_3[board[i][j]] = i
        
        return True
        

                

        