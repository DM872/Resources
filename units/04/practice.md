

## Sheet 6


### Task 1

Design a Lagrangian relaxation algorithm for the Multicommodity flow problem.

### Task 3

Consider the following problem: <!--  from [Fi2]: -->

$$
\begin{array}{lllll}
z_{IP}=&\text{max} &16x_1+10x_2+4x_4\\
&\text{s.t.}&8x_1+2x_2+x_3+4x_4\leq 10\\
&&x_1+x_2\leq 1\\
&&x_3+x_4\leq 1\\
&&0\leq x\leq 1 \qquad \text{and integer}
\end{array}
$$

1. Relax only the first constraint and calculate the Lagrangian dual
   bound.
   
2. Relax the second and third constraints and calculate the Lagrangian
   dual bound. Which among the two relaxations provides the best dual
   bound and how do they compare with respect to the dual bound given by
   the linear relaxation of the original problem IP? 


### Task 2

<!-- 
The following is based on a tutorial on Lagrangian Relaxation by J E
Beasley [JB].
--> 

Consider the following set covering problem (SCP):

$$
\vec{c} = \begin{bmatrix} 2,3,4,5 \end{bmatrix}
$$

$$
A=[a_{ij}] = \begin{bmatrix} 1& 0& 1& 0\\
 1& 0& 0& 1 \\
 0 &1 &1 &1 \\
 \end{bmatrix}
$$

Mathematically this example SCP is:

$$
\begin{array}{rrl}
\text{minimize}& 2x_1 + 3x_2 + 4x_3 + 5x_4\\
\text{s.t.}& x_1 + x_3 &\geq 1\\
 &x_1 + x_4&\geq 1\\
 &x_2 + x_3 + x_4& \geq 1\\
& x_j\in\{0,1\}&  j=1,...,4
\end{array}
$$

#### Subtask 1

Generate a Lagrangian relaxation of this SCP. Write it in general terms for a
   SCP and for the numerical example given. 

#### Subtask 2

Let the problem determined at the previous point be called LR (Lagrangian
   relaxation problem or Lagrangian lower bound problem). Consider the
   arbitrarily decided set of values for the Lagrangian multipliers
   $\lambda_1=1.5,\lambda_2=1.6,\lambda_3=2.2$.  Find the solution to the LR and
   the corresponding lower bound $z_{LR}$ to the original problem.  Is this a
   lower bound? Is the solution found for the LR feasible for the original
   problem? Is the solution found for the LR optimal for the original problem?

#### Subtask 3 

Repeat the task at the point 2. for the set of values:
   $\lambda_1=10,\lambda_2=10,\lambda_3=10$. Under what circumstances does the
   solutions to the LR being feasible for the original problem also imply that
   it is optimal for the original problem?

#### Subtask 4

Solve the Lagrangian dual problem by *subgradient optimization*. Use the
   procedure suggested by Held and Karp.

Set the step size to the value:

$$
   \theta=\mu \frac{z_{UB}-z_{LB}}{\sum_{i=1}^m (\gamma_i)^2}
$$

where $z_{LB}$ and $z_{UB}$ are the current lower bound and upper bound,
   respectively and $\mu$ an user defined parameter (try with 2 and decrease it
   throughout the iterations).

Update $\lambda_i$ using

$$
  \lambda_i=\max\{\lambda_i+\theta\gamma_i,0\}\qquad i=1,..,m
$$

Terminate when $\mu$ has converged to zero.

Is the final solution optimal for the original problem?  
