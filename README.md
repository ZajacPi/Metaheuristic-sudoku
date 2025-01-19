
# How to solve sudoku?

I am going to use *heuristic* methods to show how they can be implemented to solve it!

The goal of the project is to create an app, where you can send photo of sudoku, and it gets solved by couple of *heuristic* methods, and then the time and memmory cost is compared.

>The idea is to create a function, that we could minimise. One way ot do it is counting doubles in every column and every row, and sum it together: Now we also have a Stop Condition, our function should be equal 0!

I will use the following heuristic algorithms: 
- Simulated Anneling
- Genetic Algorithm
- Taboo Search

An example matrix:

![](/Sudoku-example.png)

And Its solution:

![](/sudoku-solution.png)

## Simulated Annealing
- Let s = s0
- For k = 0 through kmax (exclusive):
    - T ← temperature( 1 - (k+1)/kmax )
    - Pick a random neighbour, snew ← neighbour(s)
    - If P(E(s), E(snew), T) ≥ random(0, 1):
    - s ← snew
- Output: the final state s
