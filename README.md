
# How to solve sudoku?

> state of the project: not finished

I am going to use *heuristic* methods to show how they can be implemented to solve it!

The goal of the project is to create an app, where you can send photo of sudoku, and it gets solved by couple of *heuristic* methods, and then the time and memmory cost is compared.

>The idea is to create a function, that we could minimise. One way ot do it is counting doubles in every column and every row, and sum it together: Now we also have a Stop Condition, our function should be equal 0!

I will use the following heuristic algorithms: 
- Simulated Anneling
- Taboo Search
- Genetic Algorithm
- 
An example matrix:

![](/Sudoku-example.png)

And Its solution:

![](/sudoku-solution.png)

## Simulated Annealing (SA)
The idea of the algorithm came from the process of annealing metal: in higher temperature the particles behave very randomly, when it cools down the particles go in the right places which hardens the metal.
In the algorithm we constantly generate randomly neighbours of current best solution, in high temperatures we have a higher chance of considering bad solutions, the lower the temperature the stricter we are with our choice. The acceptance of bad solutions allows for exploration.

### Pseudocode
- Set initial temperature, max. num of iterations Nmax, and kmax times to try to improve in current temperature
- Generate initial solution
- For n = 0 through Nmax:
    - for k = 1 through kmax
        - Create a random neighbour by method of your choice (in sudoku I will swap two numbers within the same square)
        - If the value of the function is better for the neighbour than our best solution, it becomes the best solution
        - else, it still has a chance to become the new best sulution, with probability of exp(-(candidate_value - best_value) / T) so the lower the temperature the lower the chance
    - Lower the temperature: T ← temperature( 1 - (k+1)/kmax )
- Output: the final state s

You also can add different stop conditions, like if the solution is the same for some period or temperature goes to a certain level.


## Tabu Search (TS)
Tabu Search is another heuristic algorithm inspired by local search methods but designed to overcome their limitations, such as getting stuck in local minima. The mechanism that allows it is use of memory structures (the "Tabu List") to avoid revisiting previously explored solutions or moves. This encourages exploration of new regions in the solution space, even at the risk of temporarily accepting worse solutions.

### Core Concepts
Tabu List: A memory structure that keeps track of recently visited solutions or forbidden moves to prevent cycling.
Neighborhood Search: The algorithm generates neighboring solutions by making small changes to the current solution (e.g., swapping two numbers in Sudoku).
Aspiration Criteria: Allows overriding the Tabu status of a solution if it meets certain exceptional conditions (e.g., being better than the best solution found so far).
Termination Criteria: The algorithm stops after a fixed number of iterations or when a satisfactory solution is found.

### Pseudocode
Initialize:

- Set parameters: maximum number of iterations (Nmax) and Tabu List size (tabu_list_size).
- Initialize the Tabu List as empty.
- Start with an initial solution (best_solution) and evaluate its cost.
- For n = 0 through Nmax:
    - Generate a neighboring solution by applying a small random change to the current solution 
    - Check if the move/solution is in the Tabu List:
    - If not in the Tabu List:
        - Evaluate the neighbor's cost.
    - If the neighbor's cost is better than the current best solution, update the best solution.
    - Otherwise, still accept the neighbor as the current solution.
    - Add the move/solution to the Tabu List.
    - If the Tabu List exceeds its maximum size, remove the oldest entry.
    - Optionally, apply aspiration criteria to allow exceptional moves.
- Output the best solution and its cost.


### Stop Conditions
- A fixed number of iterations (Nmax).
- No improvement in the solution for a certain number of iterations.
- Reaching a desired quality level for the solution.

### Applications
Tabu Search is versatile and can be applied to various optimization problems, including:

- Scheduling problems (e.g., job-shop scheduling).
- Traveling Salesman Problem (TSP).
- Sudoku solving (minimizing constraint violations).
- Resource allocation and routing problems.
- Strengths and Limitations

### Strengths:

- Effective at exploring diverse areas of the solution space.
- Simple to implement and highly customizable.
- Handles large and complex solution spaces.

### Limitations:

- Relies on parameter tuning (e.g., Tabu List size, number of iterations).
- May struggle to find global optima in highly constrained problems.
- Performance can degrade if the Tabu List size is poorly chosen.

## Genetic Algorithm (GA)
Genetic Algorithm is an optimization technique inspired by the process of natural selection and genetics in biology. It is a population-based heuristic method that evolves a set of candidate solutions toward an optimal solution over multiple generations. The algorithm mimics biological operators such as selection, crossover (recombination) and mutation to improve the quality of solutions.

### Core Concepts
**Population:** A collection of candidate solutions (called individuals or chromosomes) to the optimization problem.
Fitness Function: A measure of how "good" a solution is based on the problem's objectives. Higher fitness means a better solution.

**Selection:** The process of choosing individuals from the current population to create offspring for the next generation. Higher fitness increases the chances of selection.

**Crossover (Recombination):** A genetic operator that combines two parent solutions to produce offspring with characteristics of both parents.

**Mutation:** A genetic operator that introduces small random changes in an individual to maintain diversity and explore new solutions.

**Elitism:** Ensures that the best solutions from the current generation are carried forward to the next.
