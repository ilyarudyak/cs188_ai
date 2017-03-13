## questions 1-4
* **what task do we solve?** we are searching for a single dot in a maze 
(basically we're looking for a solution of a maze - we stop when we reach 
goal state: `if problem.isGoalState(node): return path`)
* **what algorithm do we use?** we use exactly the same algorithms that is 
presented in the assignment; (a) choose a data structure (DS) and put start state in it;
(b) in a loop: pop a node from DS and push its children to DS; we also use set to
monitor nodes that we already visited; (c) to calculate path to the goal we actually
push to DS a tuple: `(child_node, path + [action])`
* **what algorithm do we implement?** we implement DFS, BFS, UCS and A* search 
(in the file `search.py`);
* **how to run this solution in pacman?** `python2 pacman.py -l tinyMaze -p SearchAgent`
* we use universal methods for DFS, BFS (we choose DS) and for UCS and A* (we choose 
heuristic, in case UCS it `nullHeuristic`) searches;

## question 5
* **what is the problem here?** we have 4 food dots in corners of the maze and 
have to find them all;
* **what heuristic do we use?** `max manhattan distance` to remaining corners;
why is that? max heuristic is admissible - see slide 28 of lecture 3 (2016);
* **how do we represent state?** as a tuple `(state, '0101')` where `'0101'` represents
visited corners; 
