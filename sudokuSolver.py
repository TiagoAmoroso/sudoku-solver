
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



def valid(board, num, pos, debug = False):
    '''Checks if the current "board" is valid with the insertion of "num(ber)" at "pos(ition)" '''

    #Checking row
    for number in range(len(board[pos[0]])):
        if board[pos[0]][number] == num and number != pos[1]:
            if debug:
                print('Row ' + str(pos[0]) + ' not valid') #DEBUG
            return False

    #Checking column
    for number in range(len(board)):
        if board[number][pos[1]] == num and number != pos[0]:
                if debug:
                    print('Column ' + str(pos[1]) + ' not valid') #DEBUG
                return False

    #Checking box
    box_row = pos[0] // 3 #Integer division returns an int and not a float
    box_column = pos[1] // 3 #Integer division returns an int and not a float
    #print(box_row, box_column) #y,x

    for row in range(box_row * 3, box_row * 3 + 3):
        for column in range(box_column * 3, box_column * 3 + 3):
            if board[row][column] == num and row != pos[0] and column != pos[1]:
                if debug:
                    print(str(board[row][column]) + ' at position (row/col): ' + str(pos[0]) + pos[1] + ' is equal to ' + str(num) + ' at position (row/col): ' + str(row) + str(column))
                    print('Box (' + str(box_row) + ',' + str(box_column) + ') is not valid') #DEBUG
                return False

    return True
    

def printBoard(board):
    '''Displaying a sodoku board that is in an array format [[row1], [row2], [row3]...etc], in the terminal'''

    for row in range(len(board)): #Iterates through each row in the board
        print('') #This moves each row onto a new line
        if row % 3 == 0 and row != 0: #Prints a seperator row every third row
            for i in range(len(board[row])):
                print(' -', end = '')
            print('')

        for number in range(len(board[row])): #Iterates through each number in the current row
            if number % 3 == 0 and number != 0: #Prints a seperator column every third column
                print('|', end = '')
            print(board[row][number], end = ' ') #Prints the current number with a space afterwards for readability purposes
    

def findEmpty(board):
    '''Returns the coordinates of the first empty space in the sodoku board, in the format (y, x) / (row, column) 
    as that is how the array is formatted'''

    for row in range(len(board)): #Iterates through each row on the board
        for number in range(len(board[row])): #Iterates through each number in the current row
            if board[row][number] == 0: #Checks if the current number is empty
                return(row, number) #Returns the coordinates of the first empty spot on the board (row, column)


def solve(board):
    emptyCell = findEmpty(board) #EmptyCell is allocated the coordinates of the first empty cell on the board

    if not emptyCell: #If there is no empty cell on the board, the puzzle can be considered to be solved
        #print('\n\nThe puzzle has been solved!')
        return True

    else: #If there is still an empty cell on the board, the puzzle is yet to be solved
        row, column = emptyCell #Setting the coordinates of the first empty cell on the board
        for num in range(1,10): #Iterating through all the possible numbers to be entered into the empty cell
            if valid(board, num, emptyCell): #Checks if the board is valid once we insert the number into the empty cell
                board[row][column] = num #Sets the empty cell equal to the number once it is known to be a valid possibility

                if solve(board): #Recursively checks if the board is solved and returns True when it is solved
                    return True  #This calls the code back to the begining of the solve function every time solve returns False
                
                else: #If the board is not solved, we reset the value of the empty cell to 0 so we try another value in it
                    board[row][column] = 0
                    

        return False

if __name__ == '__main__':
    printBoard(board)
    solve(board)
    print("\n")
    printBoard(board)