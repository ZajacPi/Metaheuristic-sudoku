import random

sudoku = [[0, 1, 0, 6, 3, 0, 0, 0, 4],
          [0, 0, 6, 0, 0, 0, 0, 0, 0],
          [2, 5, 0, 0, 0, 9, 0, 0, 3],
          [0, 9, 8, 7, 4, 0, 3, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 7, 0, 2, 1, 8, 9, 0],
          [6, 0, 0, 2, 0, 0, 0, 1, 8],
          [0, 0, 0, 0, 0, 0, 4, 0, 0],
          [7, 0, 0, 0, 1, 4, 0, 5, 0]]


def sudoku_fun(sudoku):
    rows_sum = 0
    cols_sum = 0
    for row in sudoku:
        found_numbers = []
        for element in row:
            if element not in found_numbers:
                found_numbers.append(element)
            else:
                rows_sum += 1
        
    for j in range(len(sudoku[0])):
        found_numbers = []
        for i in range(len(sudoku[0])):
            if sudoku[i][j] not in found_numbers:
                found_numbers.append(sudoku[i][j])
            else:
                cols_sum += 1
    
    return rows_sum + cols_sum


print(sudoku_fun(sudoku))
            
def SA_algorithm(fun, Tmax):
    #let's generate an initial state by making a random choice
    sudoku_size = len(sudoku[0])
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            if sudoku[i][j] == 0:
               sudoku[i][j] = random.randint(1, sudoku_size)
    
    best_solution, best_value = sudoku, sudoku_fun(sudoku)
    
    for k in range(0, Tmax):
        T = 1-((k+1)/(Tmax))
    candidate = 0
    candidate_value = fun(candidate)
    if candidate < best_value:
        best_solution, best_value = candidate, candidate_value
    #decide wether to change to worse solution
    else:
        
    