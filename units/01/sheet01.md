# Sheet 1


## Task 1

Solve some of the troublesome problems from [KN1] with Gurobi and other solvers
(soplex, glpsol) and analyze the logs.

## Task 2

Reconsider the example used to illustrate the interior-point algorithm in Sec.
8.4 of [HL] (file `HL_sec_8_4.pdf`). Suppose that $(x1, x2) = (1, 3)$ were used
as the initial feasible trial solution.  Perform one or two iterations using
`numpy`, starting from this solution. Then, write a python script to automatize
the process. Finally, solve this problem:

$$
\begin{array}{rl}
\text{maximize} \\;\\;&2x_1 + 3x_2 + 2x_3 \\
\text{subject to} \\; \\; &x_1 + x_2 +2x_3 = 3\\
&x_1,x_2,x_3 \geq 0.
\end{array}
$$

using as starting solution $[x_1, x_2, x_3]=[1, 3\/2, 1\/4]$.

How should the algorithm change if the problem was a minimization problem?

## Task 3

<!--
A person infected with Coronavirus is located at one node $p$ in a
network $G$ of social contacts and persons at risk who should avoid
being infected are located at nodes denoted by the set $S\subseteq
V\setminus{p}$. Let $u_{ij}$ be the effort required to avoid that
persons $i$ and $j$ from the network meet physically. The problem is
to determine the minimal effort required to block the physical contact
between persons in the network such that the infection does not reach
the persons at risk. How can you solve this problem in polynomial
time?
-->

Consider the [Feature Selection
case](https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/linear_regression/l0_regression.ipynb).

Implement the Lasso version together with minimizing the least absolute error. Solve the linear programming problem and analyze the solution process in the light of the article [KN1].

Implement the Lasso version (L1-norm as regularization component added to the objective function) together with minimizing the least absolute error instead of the square of residuals as done in the notebook. 

- Solve the linear programming problem in training and analyze the solution process in the light of the article [KN1]. 
- Compare the accuracy of the L1-norm and the L0-norm approach presented in the document.
