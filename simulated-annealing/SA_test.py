import random
import math
import copy

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
    '''
    Calculates the cost of the sudoku by counting duplicates in rows and columns
    '''
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

            
def SA_algorithm(sudoku, T, n, alpha, Nmax):
    '''
    fun - function that we want to minimise
    T - the initial temperature (how to choose initial temperature is complex)
    n - number of iterations before lowering the temperature
    alpha - cooling rate (value in range (0, 1))
    Nmax - maxinmum number of iterations
    '''
    
    #let's generate an initial state by making a random choice, by filling the 3x3 boxes with missing numbers randomly
    # that way, we have duplicates only in rows and cols
    
    
    sudoku_size = len(sudoku[0])
    
    # for i in range(sudoku_size):
    #     for j in range(sudoku_size):
    #         if sudoku[i][j] == 0:
    #            sudoku[i][j] = random.randint(1, sudoku_size)
    number_base = [x for x in range(1, sudoku_size+1)]
    square_size = int(math.sqrt(sudoku_size))
    all_empty_slots = []
    for k in range(square_size):
        for l in range(square_size):
            missing_numbers = number_base[:]
            empty_slots = []
            for i in range(square_size):
                for j in range(square_size):
                    if sudoku[3*k + i][3*l + j] in number_base:
                        missing_numbers.remove(sudoku[3*k + i][3*l + j])
                    else:
                        empty_slots.append((3*k+i, 3*l+j))
            #found all the missing numbers, now lets put them randomly!
            for coordinates in empty_slots:
                #mabye use random.choice?
                num = random.randrange(0, len(missing_numbers))
                sudoku[coordinates[0]][coordinates[1]] = missing_numbers[num]
                missing_numbers.pop(num)
                
            # remember the empty slots for the current square
            all_empty_slots.append(empty_slots[:])
                
    best_solution, best_value = sudoku, sudoku_fun(sudoku)
    k = 1
    
    while k < Nmax and best_value > 0:
        for i in range(0, n):
            #for the candidate, we switch two numbers in a randomly selected square
            candidate = copy.deepcopy(best_solution)
            
            random_square = random.choice(all_empty_slots)

            slot1, slot2 = random.sample(random_square, 2)

            candidate[slot1[0]][slot1[1]], candidate[slot2[0]][slot2[1]] = candidate[slot2[0]][slot2[1]], candidate[slot1[0]][slot1[1]]
             
            candidate_value = sudoku_fun(candidate)
            
            if candidate_value < best_value:
                best_solution, best_value = candidate, candidate_value
                
            #decide wether to change to worse solution by checking acceptance probability
            elif T> 1:
                probability = math.exp(-(candidate_value - best_value) / T)
                if random.random() <= probability:
                   best_solution, best_value = candidate, candidate_value
        if T > 1:
            # after n tries, we lower the temperature and increase the counter  
            T = T*alpha 
        k+= 1
        if k%50 == 0:
            print(f"T={T}: {best_value}")
            
    print(best_solution)
    print(best_value)

SA_algorithm(sudoku, 10000, 200, 0.99, 3000)
