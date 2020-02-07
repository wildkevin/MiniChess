def printBoard(board):
    print("   ", end = "")
    for i in range(0, len(board[0])):
        print(str(i)+" ", end = "")
    print("\n")
    row = 0
    for r in board:
        print(row, " ", end = "")
        for c in r:
            if c == 1:
                print("w ", end = "")
            elif c == 2:
                print("b ", end = "")
            else:
                print("- ", end = "")
        print()
        row = row + 1
    print()
            
def makeInitBoard(dim):
    board = []
    for i in range(0,dim):
        row = []
        for j in range(0,dim):
            row.append(0)
        board.append(row)
    for i in range(0,dim):
        board[0][i] = 1
        board[dim - 1][i] = 2
    return board

def miniChess():
    from random import randint
    print("Welcome to miniChess\nHere are the rules...\n1. White moves first\n2. Pawn can move straight ahead one space if that space is empty\n"
          "3. Pawn can move diagonally one space forward to capture opponent’s pawn occupying that space\n4. You win if you capture all of your opponent's pawns\n"
          "5. You win if one of your pawns reaches the opposite end of the board\n6. You win if your opponent can’t move")
    while True:
        dim = input("What size board would you like? \n(enter an integer greater than 2): ")
        try:
            if int(dim) > 2:
                dim = int(dim)
                bheight = dim
                bwidth = dim
                b = makeInitBoard(dim)
                break
        except:
            pass
    print("\nHere's the initial board...\n")
    printBoard(b)
    while True:
        answer = input("Choose the white pawns or black pawns (enter 'w' or 'b' or 'quit'): ")
        if answer == "w":
            mycolor = 2
            oppo = 1
            break
        if answer == "b":
            mycolor = 1
            oppo = 2
            break
        if answer == "quit":
            print("Ending the game")
            return
    if mycolor == 1:
        print("Here's my opening move...\n")
        column = randint(0, bwidth - 1)
        b[1][column] = b[0][column]
        b[0][column] = 0
        printBoard(b)
    while True:
        while True:
            test_point = ""
            try:
                print("\nEnter the coordinates of the pawn you wish to move:")
                fromrow = int(input("   row: "))
                fromcol = int(input("   col: "))
                print("Enter the coordinates of the destination square: ")
                torow = int(input("   row: "))
                tocol = int(input("   col: "))
                if b[fromrow][fromcol] == oppo:
                    if oppo == 2 and fromrow == torow + 1 and fromcol == tocol and b[torow][tocol] == 0:
                        test_point = 1
                    if oppo == 1 and fromrow == torow - 1 and fromcol == tocol and b[torow][tocol] == 0:
                        test_point = 1
                    if oppo == 1 and fromrow == torow - 1 and fromcol == tocol -1 and b[torow][tocol] == 2:
                        test_point = 1
                    if oppo == 2 and fromrow == torow + 1 and fromcol == tocol - 1 and b[torow][tocol] == 1:
                        test_point = 1
                    if oppo == 1 and fromrow == torow - 1 and fromcol == tocol + 1 and b[torow][tocol] == 2:
                        test_point = 1
                    if oppo == 2 and fromrow == torow + 1 and fromcol == tocol + 1 and b[torow][tocol] == 1:
                        test_point = 1
                test_point += 1
                b[torow][tocol] = b[fromrow][fromcol]
                b[fromrow][fromcol] = 0
                break
            except:
                print("Not a valid move\nPlease choose again")
        print("This is your move...\n")
        printBoard(b)
        mypossiblemoves = move_maker(b, mycolor)
        if mypossiblemoves == []:
            print("I can't move\nCongratulations! You win!")
            return
        for j in range(dim):
            if oppo == 2 and b[0][j] == oppo:
                print("I can't move\nCongratulations! You win!")
                return
            if oppo == 1 and b[dim-1][j] == oppo:
                print("I can't move\nCongratulations! You win!")
                return
        b = move_chooser(mypossiblemoves, mycolor) 
        print("Here's my response...\n")
        printBoard(b)
        oppopossiblemoves = move_maker(b, oppo)
        if oppopossiblemoves == []:
            print("You lose\nTry Again!")
            return
        for i in range(dim):
            if mycolor == 2 and b[0][i] == mycolor:
                print("You lose\nTry Again!")
                return
            if mycolor == 1 and b[dim-1][i] == mycolor:
                print("You lose\nTry Again!")
                return

def move_maker(board, color):
    '''compute all the possiblemoves of 'color' with the certain board input'''
    import copy
    possiblemoves = []
    dim = len(board)
    if color == 2:
        for i in range(0,dim):
            for j in range(0,dim):
                newboard = copy.deepcopy(board)
                if board[i][j] == 2 and i > 0:
                    if board[i-1][j] == 0:
                        newboard[i][j] = 0
                        newboard[i-1][j] = 2
                        possiblemoves.append(newboard)
        for i in range(0,dim):
            for j in range(0,dim):
                newboard = copy.deepcopy(board)
                if board[i][j] == 2 and i > 0 and j > 0: 
                    if board[i-1][j-1] == 1:
                        newboard[i][j] = 0
                        newboard[i-1][j-1] = 2
                        possiblemoves.append(newboard)
        for i in range(0,dim):
            for j in range(0,dim):
                newboard = copy.deepcopy(board)
                if board[i][j] == 2 and j <= (dim - 2) and i > 0:
                    if board[i-1][j+1] == 1:
                        newboard[i][j] = 0
                        newboard[i-1][j+1] = 2
                        possiblemoves.append(newboard)
    if color == 1:
        for i in range(0,dim):
            for j in range(0,dim):
                newboard = copy.deepcopy(board)
                if board[i][j] == 1 and i <= (dim -2):
                    if board[i+1][j] == 0:
                        newboard[i][j] = 0
                        newboard[i+1][j] = 1
                        possiblemoves.append(newboard)
        for i in range(0,dim):
            for j in range(0,dim):
                newboard = copy.deepcopy(board)
                if board[i][j] == 1 and i <= (dim-2) and j <= (dim-2): 
                    if board[i+1][j+1] == 2:
                        newboard[i][j] = 0
                        newboard[i+1][j+1] = 1
                        possiblemoves.append(newboard)
        for i in range(0,dim):
            for j in range(0,dim):
                newboard = copy.deepcopy(board)
                if board[i][j] == 1 and i <= (dim - 2) and j > 0:
                    if board[i+1][j-1] == 2:
                        newboard[i][j] = 0
                        newboard[i+1][j-1] = 1
                        possiblemoves.append(newboard)
    return possiblemoves

def move_chooser(possiblemoves, color):
    '''choose the best move fromm all the possiblemoves of 'color'''
    dim = len(possiblemoves[0])
    num = len(possiblemoves)
    code = {}
    result = []
    test = 0
    if color == 1:
        end = dim-1
        oppo = 2
    elif color == 2:
        end = 0
        oppo = 1
    for i in range(0,num):
        for j in range(0,dim):
            if possiblemoves[i][end][j] == color:
                choose = possiblemoves[i]
                test = 1
    for i in range(0,num):
        if move_maker(possiblemoves[i], oppo) == []:
            choose = possiblemoves[i]
            test = 1
    if test == 0:
        for i in range(0,num):
            total = 0
            for j in range(0,dim):
                total = total + sum(possiblemoves[i][j])
            code[total] = possiblemoves[i]
            result.append(total)
            choose = code[min(result)]
    return choose

if __name__ == "__main__":
    miniChess()