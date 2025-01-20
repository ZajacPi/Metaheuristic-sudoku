import random
import math
import copy

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

def generate_initial_state(sudoku):
    '''
    Function that generates initial state for a sudoku, by filling the empty gaps in the square with the numbers
    that are missing (in a square there should be all numbers from 1 to 9)
    
    It makes sure there are no duplicates within one square.

    It also saves the ampty positions in all_empty_slots: that are the only places that the algorithm can change, 
    the initially filled gaps are fixed
    '''
    
    
    sudoku_size = len(sudoku[0])
    
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
            for coordinates in empty_slots:
                num = random.choice(missing_numbers)
                sudoku[coordinates[0]][coordinates[1]] = num
                missing_numbers.remove(num)
                
            # remember the empty slots for the current square
            all_empty_slots.append(empty_slots[:])
            
    return sudoku, sudoku_fun(sudoku), all_empty_slots
                
def SA_algorithm(sudoku, T, k, alpha, Nmax):
    '''
    fun - function that we want to minimise
    T - the initial temperature (how to choose initial temperature is complex)
    k - number of iterations before lowering the temperature
    alpha - cooling rate (value in range (0, 1))
    Nmax - maxinmum number of iterations
    '''
    
    #let's generate an initial state by making a random choice, by filling the 3x3 boxes with missing numbers randomly
    # that way, we have duplicates only in rows and cols
    best_solution, best_value, all_empty_slots = generate_initial_state(sudoku)
    n = 1
    
    while n < Nmax and best_value > 0:
        for i in range(0, k):
            ######################### what if in the same temperature we should analise the same base best, and create neighbours for it? because now in the same temp I create neighbours for neighbours
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
        n += 1
        if n%50 == 0:
            print(f"T={T}: {best_value}")
            
    print(best_solution)
    print(best_value)

if __name__ == "__main__":
    sudoku = [[0, 1, 0, 6, 3, 0, 0, 0, 4],
              [0, 0, 6, 0, 0, 0, 0, 0, 0],
              [2, 5, 0, 0, 0, 9, 0, 0, 3],
              [0, 9, 8, 7, 4, 0, 3, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 7, 0, 2, 1, 8, 9, 0],
              [6, 0, 0, 2, 0, 0, 0, 1, 8],
              [0, 0, 0, 0, 0, 0, 4, 0, 0],
              [7, 0, 0, 0, 1, 4, 0, 5, 0]]
    SA_algorithm(sudoku, 10000, 200, 0.99, 3000)
