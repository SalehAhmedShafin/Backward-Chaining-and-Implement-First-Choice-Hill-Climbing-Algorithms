# Backward-Chaining-and-Implement-First-Choice-Hill-Climbing-Algorithms

Backward Chaining Algorithm:

Backward chaining is a reasoning or inference strategy used in artificial intelligence and expert systems to deduce a sequence of steps or facts that lead to a desired goal or conclusion. It is often employed in rule-based systems, where a set of rules and a specific goal are given, and the system works backward from the goal to determine which rules need to be applied in order to reach that goal.

In a backward chaining algorithm, the process starts with the goal or conclusion that needs to be proven. The algorithm then examines the available rules and facts to find those that support the goal. If a rule's conclusion matches the current goal, the algorithm moves to its premises or antecedents and tries to prove them. This process continues recursively until either the goal is proven or no further rules can be applied.

Input:
goal, facts, rules, db =["M"], ["A", "B", "C", "D"], [<br>
[("P"),"Q"],<br>
[("D","M"),"P"],<br>
[("B","L"),"M"],<br>
[("A","B"),"L"],<br>
[("A","D"),"G"],<br>
[("G","B"),"C"]], {}

Implementation Steps:

1. Call Backward Chaining recursive function with goals, rules, facts and database
2. Check if the goal is already in the database,
    if true, then add goal to the result
3. Check if goal is already in facts,[base condition]
    if true, then add True to the result

4. Iterate through rules, Check if the rule's conclusion is the goal,
    if true, check if all the rule's premises are true by calling the recursive function,
    if all premises are true, add the goal to the database and return True
5. if no rule is found or no rule's premises are true, add False to the result and
    database

First Choice Hill Climbing Algorithm:

Hill climbing is a heuristic optimization algorithm used to find the optimal solution for a given problem by iteratively moving toward better solutions in the solution space. The "hill" metaphor reflects the idea of climbing a hill (maximizing or minimizing a function) to reach the highest point (optimal solution).

The First Choice Hill Climbing Algorithm is a variant of the basic hill climbing approach. In this algorithm, at each step, instead of exhaustively evaluating all possible neighboring solutions and selecting the best one, the algorithm chooses the first neighboring solution that improves the current solution. If this chosen solution results in a better outcome, it becomes the new current solution, and the process continues. However, if no better solution is found among the neighbors of the current solution, the algorithm terminates.

One of the challenges with the First Choice Hill Climbing Algorithm is that it can get stuck in local optima—solutions that are better than their immediate neighbors but not necessarily the global optimum. Since the algorithm doesn't explore all possible neighbors, it might miss out on better solutions that are farther away in the solution space. This limitation has led to the development of more sophisticated optimization techniques, such as simulated annealing, genetic algorithms, and particle swarm optimization, which aim to overcome local optima problems.

Input:
ss = [ 2, 3, 4, 5, 6, 5, 7, 8 ]

Implementation Steps:<br>
Defined a function called ‘fchc’ which works as follows:<br>
• Initialize Current State and Current Heuristic Value<br>

• Find Successors of the Current State<br>

• Find Heuristic Value for the Successors<br>

• If Any Successors heuristic value is lower than current value. Then this state will become current state and its heuristic value will become current value. Add this state to database<br>
with status = “c”<br>

• Otherwise Add that state to database with status = “s”<br>

• If No Successors with lower heuristic value is found and current value is not zero, then<br>
generate a random state and restart the process<br>

• Otherwise print the state and return.<br>
