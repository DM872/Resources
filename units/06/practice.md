# Practice on Multi Depot Vehicle Scheduling

In the directory `MDVS` you find the files `sample.inp` and `m4n500s0.inp` that
contain data about timetabled trips housed in different depots.  The name of the
file indicates the number of depots $m$, the number of trips $n$ and finally the
identifier of the instance $0,1,2,3,4$. Trips are identified by numbers from $m$
to $n+m−1$ and indexed by $i$ that runs through the same range of numbers. The
format of the files is as follows:

```python
(first line) m <tab> n <tab> for each depot the maximum number of vehicles

(second line and further) cost matrix of size (m + n) x (m + n). The
number in row i, column j indicates

- if i <= m and j > m: the cost of pull-out trip from depot i to trip j-m
  (including 50% of fixed cost for the vehicle),
- if i > m and j <= m: the cost of pull-in trip from trip i-m to depot j
  (including 50% of fixed cost for the vehicle),
- if i > m and j > m: the cost of performing trip j-m after trip i-m.

A -1 indicates that it is infeasible to perform trip j after trip
i. Note that, i <= m and j <=m has no meaning and there are all -1's
there.
```

The instance `sample.inp` is a small toy instance used in class for the
lecture that may be used for debugging or visualization purposes.

In the repository you find also the python script
`mdvs-template.py`. It contains the function `readData` that reads the
input data file and populates a list `Ts` with every arc.
<!-- This list is used to build a tuplelist, which is a Gurobi sub-class. -->
It then
contains the code that implements the multi-depot model (24)–(28) of
slide 35.

## Task 1

Inspect the python file `mdvs-template.py` and make sure you understand it.

## Task 2

Run the script `mdvs-template.py` on the small instance `m4n500s0.inp` and observe the output produced. Explain what happened and fill in the table below:

|--------------------------------+------------------------+-----------------------------+-------------|
| Capacity                       | 	62, 59, 56, 56 | 	45,45,45,45	 | 20,20,20,20 |
|--------------------------------+------------------------+-----------------------------+-------------|
| Linear Programming lower bound |                        |                             |             |
| Integer Optimal solution       |                        |                             |             |
| Number of vehicles used        |                        |                             |             |
| Number of depots used          |                        |                             |             |
|--------------------------------+------------------------+-----------------------------+-------------|

Tips:

To define binary variable you can use:
```
model.addVar(vtype="B")
```
To ignore the integrality constraint you can set the variable as continuous:
```
model.addVar(lb=0.0, ub=1.0, vtype="C")
```


## Task 3

In the table we used the linear relaxation as lower bound. Another
convenient way to obtain a lower bound is by relaxing some constraints
that make the problem easy to solve. In the lecture we arrived at the
multi-depot model incrementally. In particular, we saw that we had to
add some constraints that broke the amenable min cost flow structure of
the problem. Locate these constraints in the script and assess the lower
bound obtained by relaxing them and solving the min cost flow problem
left. Is this lower bound better or worse than the linear relaxation
lower bound?  


## Task 4

What is a lower bound on the sum of the capacities of the
depots such that a feasible solution is guaranteed to exist? Implement
the model that we saw in class that determines such lower bound.
Download now the larger instance `m4n1500s0.inp` and try to solve it again
with the original multi-depot model. What does it happen?  Instead of
solving a unique huge model, it is good practice to decompose a problem
into smaller simpler subproblems. Download now the script
`lagrangian-template.py` that contains elements to implement a Lagrangian
relaxation approach. Consider the Lagrangian relaxation (29)–(32) of
slide 37. Write a python function that solves $\phi(\lambda)$, that is a function
that solves a Min Cost Flow problem with the arc costs defined as a
function of the h-th depot and of $\lambda$ as in (37) in slide 40.

## Task 5

Once you a wrote such a script, use it to solve the subproblems and to
compute a lower bound for the following values of vector $\lambda$:

|------------------------------------------------+-------------|
|                                                | Lower Bound |
|------------------------------------------------+-------------|
| all elements equal to 100                      |             |
| all elements equal to 1000                     |             |
| elements are random real numbers from [0,1000] |             |
|------------------------------------------------+-------------|

Are they all valid lower bounds? Can you devise a procedure to find the
values for $\lambda$ that give the greatest possible lower bound?


## Task 6


Using the preimplemented skeleton available in
`lagrangian-template.py`, compute the optimal Lagrangian multipliers
by developing a basic subgradient algorithm (see Algorithm 1 in slide
42).


## Task 7

Implement a greedy heuristic that starting from the optimal continuous
relaxation, builds a feasible solution (slide 43).  Tips: use the
method: `lagrangian_heuristic` in `lagrangian-template.py` and complete it
with the missing parts. You will need a model used earlier in this
exercise.


## Task 8

[Optional] Using the same data, try to develop a basic column generation
algorithm, using the Set Partitioning formulation based on path
variables. In order to solve the pricing subproblem, you can either
formulate the shortest path as an LP (exploiting total unimodularity) or
use a shortest path algorithm from the NetworkX python library. As
starting variables you may use a path for each depot and each trip that
cover a single trip.  Once the algorithm stops (there are no more
negative reduced cost path), you can solve an Integer Linear problem
defined only on the set of generated columns. How large is the gap from
the LP solution and the integer solution?
