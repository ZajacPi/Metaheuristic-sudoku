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

### I will try to do it with objects, that contain the sudoku version, calsulated solution, and empty space 
class Child:
    def __init__(self, board, cost):
        self.board = board
        self.cost = cost

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
            #found all the missing numbers, now lets put them randomly!
            for coordinates in empty_slots:
                num = random.choice(missing_numbers)
                sudoku[coordinates[0]][coordinates[1]] = num
                missing_numbers.remove(num)
                
            # remember the empty slots for the current square
            all_empty_slots.append(empty_slots[:])
            
    return sudoku, sudoku_fun(sudoku), all_empty_slots

# I have problem with mating, in this approach where the numbers in a square are fixed it might not work
####################################################
def Genetic_Algorithm(sudoku, population_size, Nmax):
    '''
    sudoku - a list of lists sudoku with zeros in empty spaces
    population_size - how many childeren should we generate?
    Nmax - maxinmum number of iterations
    '''
    generation = 1
    population = []
    best_value = float('inf')
    best_solution = None
    
    # generate initial population
    for _ in range(population_size):
        child = generate_initial_state(copy.deepcopy(sudoku))
        if child[1] == 0:
                print("Found solution!")
                return child
        population.append(child)

    n=0 
    while best_value > 0 and n < Nmax:        
        # if we didn't find a sudoku with cost 0, we generate a new, better generation
        # let's try elite-selection, 10% of best children will have a chance to become parents
        sorted_generation = sorted(population, key=lambda tup: tup[1])
        new_generation = sorted_generation[0:int(0.1 * population_size)]
        best_child = sorted_generation[0]
        
        if n % 50 == 0:
            print(f"Iteration {n}, Best Value: {best_value}")
    return best_solution
            

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
    # Solve the Sudoku
    solution = Genetic_Algorithm(sudoku, 100, Nmax=1000)

    print("\nSolved Sudoku:")
    for row in solution:
        print(row)
