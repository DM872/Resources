## Extra Sheet 


### Task 1

Write an extended formulation with extreme points and extreme rays for the polyhedron

$$
\begin{align*}
−x_1 +x_2 &\leq 1\\
3x_1 +x_2 &\geq 5 \\
x_1 +x_2  &\geq 1\\
x_1 +2x_2 &\leq 11.
\end{align*}
$$

### Task 2

Consider the mixed integer program

$$
\begin{align*}
\max\; &4x_1 +5x_2 +2y_1 −7y_2 +5y_3 \\
&3x_1 +4x_2 +2y_1 −2y_2 +3y_3\leq 10\\
&\vec x\leq 3,\; \vec x\in \mathbb{Z}^2_+,\; \vec y\leq 2,\; \vec y\in \mathbb{R}^3_+. 
\end{align*}
$$

Solve it using Benders’ algorithm. A template for the implementation is
avaialble in the `code` directory.

After solving it, you are informed that the $y$ variables should also be integer.
Without starting again from scratch:

  1. Solve the new problem using a basic branch and bound algorithm (Section 12.5.1)
  2. Solve using no-good cuts (Section 12.5.2).
