from main import sudokuSolver
from main import elimination

def tester(a, b=True):
    return "You Passed!" if a == b else "You Failed!"

def instantiateCases () :
    # Correctly Formulated Sudoku
    global s 
    s = [[0,0,7, 0,0,0, 0,1,5],
         [0,0,0, 3,9,7, 0,0,0],
         [0,6,2, 0,1,0, 4,0,9], 
         
         [0,2,0, 0,0,1, 5,4,3],
         [7,0,0, 4,0,9, 0,0,1],
         [4,8,1, 2,0,0, 0,6,0],
         
         [9,0,6, 0,2,0, 7,3,0],
         [0,0,0, 9,8,4, 0,0,0],
         [1,5,0, 0,0,0, 2,0,0]
        ]    
    # Unsolvable Sudoku (Information Missing)
    global s2 
    s2= [[0,0,0, 0,0,0, 0,1,5],
         [0,0,0, 3,9,7, 0,0,0],
         [0,0,0, 0,1,0, 4,0,9],
         [0,0,0, 0,0,1, 5,4,3],
         [0,0,0, 4,0,9, 0,0,1],
         [0,0,0, 2,0,0, 0,6,0],
         [0,0,0, 0,2,0, 7,3,0],
         [0,0,0, 9,8,4, 0,0,0],
         [0,0,0, 0,0,0, 2,0,0]
        ]
    # Solved Sudoku
    global s3 
    s3= [[8,9,7, 6,4,2, 3,1,5],
         [5,1,4, 3,9,7, 6,8,2],
         [3,6,2, 5,1,8, 4,7,9],
         [6,2,9, 8,7,1, 5,4,3],
         [7,3,5, 4,6,9, 8,2,1],
         [4,8,1, 2,5,3, 9,6,7],
         [9,4,6, 1,2,5, 7,3,8],
         [2,7,3, 9,8,4, 1,5,6],
         [1,5,8, 7,3,6, 2,9,4]]
    # Invalid Sudoku (Does not follow Rules of Sudoku
    global s4 
    s4= [[0,0,7, 0,0,0, 0,1,5],
         [0,0,0, 3,9,7, 0,0,0],
         [0,6,2, 0,1,0, 4,0,9], 
         [0,2,0, 0,0,1, 5,4,3],
         [7,0,0, 4,0,9, 0,0,1],
         [4,8,1, 2,0,0, 0,6,0],
         [9,0,6, 5,2,0, 7,3,0],
         [0,0,0, 9,8,4, 0,0,0],
         [1,3,6, 0,0,0, 2,0,0]
        ]
    # s after one full application of elimination
    global s5 
    s5=[[0,0,7, 0,0,0, 0,1,5],
        [0,0,0, 3,9,7, 0,0,0],
        [0,6,2, 0,1,0, 4,0,9],
        [6,2,9, 0,7,1, 5,4,3],
        [7,3,5, 4,6,9, 8,2,1],
        [4,8,1, 2,0,0, 9,6,7],
        [9,4,6, 0,2,5, 7,3,8],
        [0,7,3, 9,8,4, 0,5,6],
        [1,5,8, 0,3,6, 2,9,4]]
        

instantiateCases()
print("Test Case #1:", tester(sudokuSolver(s, [elimination]), s3))
instantiateCases()
print("Test Case #2:", tester(sudokuSolver(s5, [elimination]), s3))
instantiateCases () 
try :
    sudokuSolver(s2, [elimination])
    print("Test Case #3: You Failed!")
except Exception:
    print("Test Case #3: You Passed!")
instantiateCases () 
try :
    sudokuSolver(s4, [elimination])
    print("Test Case #3: You Failed!")
except Exception:
    print("Test Case #4: You Passed!")