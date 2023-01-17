from Exceptions import SudokuUnsolvable
from Exceptions import SudokuInvalid

def solved(s) :
    for i in s:
        for j in i:
            if j == 0:
                return False
    return True

def horizontalCheck(x, val, s):
    for cell in s[x]:
        if cell == val:
            return False
    return True

def verticalCheck(y, val, s) :
    for cell in range (len(s)):
        if s[cell][y] == val:
            return False
    return True

def subSquareCheck(x,y,val,s) :
    startX = 0
    startY = 0
    
    if x <= 3:
        startX = 0
    elif x <= 6:
        startX = 3
    else: 
        startX = 6
    
    if y <= 3:
        startY = 0
    elif y <= 6:
        startY = 3
    else:
        startY = 6
    for row in range(3):
        for column in range(3):
            if s[startY+row][startX+column] == val:
                return False
    
    return True

def elimination (x, y, s) :
    possible = []
    for num in range (9):
        if subSquareCheck(x+1,y+1,num +1,s) and verticalCheck(x, num+1, s) and horizontalCheck(y, num+1, s):
            possible += [num +1]
            
    if len(possible) == 1:
        return possible[0]
    elif len(possible) > 1: return 0
    else: 
        raise SudokuInvalid 

def applyStrategy(strategy, s) :
    change = False
    if not solved(s):
        for row in range(9):
            for column in range(9):
                if s[row][column] == 0:
                    try:
                        if strategy(column, row, s) != 0: 
                            s[row][column] = strategy(column, row, s)
                            change = True
                    except:
                        return False
    else: return False
    return change

def sudokuSolver (s, strategies) :
    while not solved(s):
        change = False
        for i in strategies:
            if applyStrategy(i, s):
                change = True
        if not change:
            raise SudokuUnsolvable
    return s
