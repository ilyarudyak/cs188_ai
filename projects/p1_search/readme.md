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

## questions 5-6
* **what is the problem here?** we have 4 food dots in corners of the maze and 
have to find them all;
* **what heuristic do we use?** `max manhattan distance` to remaining corners;
why is that? max heuristic is admissible - see slide 28 of lecture 3 (2016);
* **how good is it?** it expands 1136 nodes and that's full credit (less than 1200);
* **how do we represent state?** as a tuple `(state, '0101')` where `'0101'` represents
visited corners; 
* **how to run this solution in pacman?** `python2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`

## question 7
* **what is the problem here?** we have to eat all the dots using A* search and appropriate 
heuristic;
* **what heuristic do we use?** again we use max heuristic - this time max manhattan distance
to food dot (in other words - distance to furthes food dot);
* **what are the result?** well we have 9551 expanded nodes and this is 3/4;
* **how to run this solution in pacman?** `python2 pacman.py -l trickySearch -p AStarFoodSearchAgent`
* **improvement** we may check if any wall between pacman and food dot, so we can get something like 8686;
it's full credit but still far away from challenge;

## question 8 
