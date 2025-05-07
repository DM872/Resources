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
\max\\; &4x_1 +5x_2 +2y_1 −7y_2 +5y_3 \\
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

### Task 3

Consider the following problem:

$$
\begin{align*}
  \min~&2x + \pi_1(y_{11} + 3y_{21}) + \pi_2(y_{12} + 3y_{22})+ \pi_3(y_{13} + 3y_{23})\\
  \text{s.t.}~&2y_{1s}+y_{2s}+x = h_{1s} & s=1,\ldots,3\\
       &-y_{1s}+y_{2s} +4x \geq h_{2s}& s=1,\ldots,3\\
       &y_{1s},y_{2s}\geq 0, s=1,\ldots,3,x\geq 0
\end{align*}
$$

$(h_1,h_2)\in \Xi=\left\{(1,2),(1,3),(2,1)\right\}$ and
$\pi_1=\pi_2=\pi_3=\frac{1}{3}$.

Solve the problem using the Benders' reformulation (L-Shaped method) and compare
its solution to that obtained without decomposing the problem. Use the code
below to get started.

```{python}
class Scenarios:
  
    def __init__(self):
        self.n_scenarios = 3
        self.probability = [1/self.n_scenarios for s in range(self.n_scenarios)]
        self.h1 = [1,1,2]
        self.h2 = [2,3,1]

scenarios = Scenarios()
print("Scenario 1 : h1=",scenarios.h1[0]," h2=",scenarios.h2[0]," probability=",scenarios.probability[0])
```