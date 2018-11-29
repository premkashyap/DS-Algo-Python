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


if __name__ == '__main__':
    print(nqueen(4))