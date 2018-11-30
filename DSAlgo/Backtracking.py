class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def nqueen(n):
    board = [[None for i in range(n)] for j in range(n)]

    def _nqueen(board, i, n):
        if i == n:
            return True
        y = 0
        while y < n:
            if (is_position_valid(board, Position(i,y))):
                board[i][y] = 1
                if(_nqueen(board, i+1, n)):
                    return True
                else:
                    board[i][y] = None
            y+=1
        return False
    
    _nqueen(board, 0, n)
    return board

def is_position_valid(board, pos):
    n = len(board)
    #horizontal check
    for i in range(pos.x):
        if board[i][pos.y] != None:
            return False
    
    #bottom angle check
    x = pos.x
    y = pos.y
    while x >= 0 and y >= 0:
        if board[x][y] != None:
            return False
        x-=1
        y-=1
    
    #top angle check
    x = pos.x
    y = pos.y
    while y < n and x >=0:
        if board[x][y] != None:
            return False
        x-=1
        y+=1

    return True

def is_number_valid(board, number, pos):
    if type(board[pos.x][pos.y]) is tuple:
        return True
    #check horizontal validity
    n = len(board)
    for i in range(n):
        current_number = board[i][pos.y][0] if type(board[i][pos.y]) is tuple else board[i][pos.y]  
        if current_number == number:
            return False
    
    #check vertical validity
    for j in range(n):
        current_number = board[pos.x][j][0] if type(board[pos.x][j]) is tuple else board[pos.x][j]
        if current_number == number:
            return False

    #check grid validity

    horizontal_box = pos.x//3
    vertical_box = pos.y//3

    for i in range(3*horizontal_box, 3*horizontal_box+3):
        for j in range(3*vertical_box, 3*vertical_box+3):
            current_number = board[i][j][0] if type(board[i][j]) is tuple else board[i][j]
            if current_number == number:
                return False

    return True

def sudoku(board):
    def _sudoku_solver(board, pos):
        n = len(board)
        if pos.x == n or pos.y == n:
            return True
        if(board[pos.x][pos.y] is not None and type(board[pos.x][pos.y]) is tuple):
            if pos.y < n-1 :
                return _sudoku_solver(board, Position(pos.x, pos.y+1))
            else:
                return _sudoku_solver(board, Position(pos.x+1, 0))
        else:
            for num in range(1,n+1):
                if (is_number_valid(board, num, pos)):
                    board[pos.x][pos.y] = num
                    if pos.y < n-1 :
                        if (_sudoku_solver(board, Position(pos.x, pos.y+1))):
                            return True
                        else:
                            board[pos.x][pos.y] = None
                    else:
                        if (_sudoku_solver(board, Position(pos.x+1, 0))):
                                return True
                        else:
                            board[pos.x][pos.y] = None
            return False
    
    _sudoku_solver(board, Position(0,0))
    return board


def print_board(board):
    n = len(board)
    for i in range(8,-1,-1):
        for j in range(n):
            value = board[i][j][0] if type(board[i][j]) is tuple else board[i][j]
            print(value, end = ' ')
        print('')
                
if __name__ == '__main__':
    board = [
         [None, None, None, None, None, (8,), None, (5,), None]
        ,[(3,), None, None, None, (1,), None, None, None, (4,)]
        ,[None, (1,), None, (7,), None, None, (2,), None, None]
        ,[None, None,(1,), None, None, (9,), None, (3,), None]
        ,[(9,), None, None, None,(4,), None, None, None, (8,)]
        ,[None, (5,), None, (3,), None, None, (7,),None, None]
        ,[None, None, (8,), None, None, (5,),None, (7,),None]
        ,[(4,), None, None, None, (8,), None, None,None,(1,)]
        ,[None, (9,), None, (2,), None, None, None,None, None]
    ]
    print_board(sudoku(board))