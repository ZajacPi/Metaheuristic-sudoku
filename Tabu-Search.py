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
            #found all the missing numbers, now lets put them randomly!
            for coordinates in empty_slots:
                #mabye use random.choice?
                num = random.randrange(0, len(missing_numbers))
                sudoku[coordinates[0]][coordinates[1]] = missing_numbers[num]
                missing_numbers.pop(num)
                
            # remember the empty slots for the current square
            all_empty_slots.append(empty_slots[:])
            
    return sudoku, sudoku_fun(sudoku), all_empty_slots


def TS_algorithm(sudoku, tabu_list_size, neighborhood_size, Nmax):
    '''
    sudoku - a list of lists sudoku with zeros in empty spaces
    tabu_list_size - maximum length of tabu list, if we fill it completely we should delete the oldest entry    
    Nmax - maxinmum number of iterations
    '''
    
    best_solution, best_value, all_empty_slots = generate_initial_state(sudoku)
    tabu_list = []
    for i in range(Nmax):
        best_candidate, best_candidate_value = None, float('inf')
        for _ in range(neighborhood_size):
            # let's generate a neighbour
            candidate = copy.deepcopy(best_solution)
            random_square = random.choice(all_empty_slots)
            slot1, slot2 = random.sample(random_square, 2)

            candidate[slot1[0]][slot1[1]], candidate[slot2[0]][slot2[1]] = candidate[slot2[0]][slot2[1]], candidate[slot1[0]][slot1[1]]
            
            # now, we have to check if he is in tabu list
            if candidate not in tabu_list:
                candidate_value = sudoku_fun(candidate)
                if candidate_value < best_candidate_value:
                    best_candidate, best_candidate_value = candidate, candidate_value
            
        # update tabu list
        tabu_list.append(best_candidate) 
        
        # check if the best neighbour is better than the overall best solution
        if best_candidate_value < best_value:
            best_solution, best_value = best_candidate, best_candidate_value

        # Debugging information
        if i % 50 == 0:
            print(f"Iteration {i}, Best Value: {best_value}")

                
        if len(tabu_list) > tabu_list_size:
                tabu_list.pop(0)
    
    print(best_value)
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
    solution = TS_algorithm(sudoku, tabu_list_size=100, neighborhood_size=50,  Nmax=1000)

    print("\nSolved Sudoku:")
    for row in solution:
        print(row)
