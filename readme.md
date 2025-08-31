# Maze Search Problems

This project implements different search algorithms to solve a maze.  
The maze is represented as a 2D grid, where:

- `X` = wall/obstacle  
- `s` = start point  
- `g` = goal point  
- `·` = path found by the algorithm  

---

## Implemented Algorithms

1. **Breadth-First Search (BFS)**  
   - Explores nodes level by level (queue-based).  
   - Guarantees the shortest path in an unweighted maze.  

2. **Depth-First Search (DFS)**  
   - Explores as far as possible along one branch before backtracking (stack-based).  
   - Does not guarantee the shortest path but can be faster in some cases.  

3. **Greedy Best-First Search (with Manhattan Distance)**  
   - Uses the Manhattan distance as a heuristic to prioritize nodes closer to the goal.  
   - Faster than BFS/DFS in many cases, but does not guarantee the shortest path.  

---

## How to Run

Run the program with Python:

python search_problems.py


You will be prompted to choose an algorithm:

Choose which algorithm to use:
(1): BFS (queue)
(2): DFS (stack)
(3): Greedy Best-First with Manhattan Heuristic


After selecting, the program will:  
1. Print the original maze.  
2. Show the chosen algorithm’s solution.  
3. Print the maze with the shortest path marked as `·`.  
4. Display the explored nodes.  

---

## Example

Input maze (simplified):

```
X X X X X
X s     X
X   X g X
X X X X X
```


Output (BFS):

```
X X X X X
X s · · X
X   X g X
X X X X X
```


Shortest path found:

[(1,1), (1,2), (1,3), (2,3), (2,4)]