# Sheet 1

## Task 1

Solve some of the troublesome problems from [KN1] with Gurobi and other solvers
(soplex, glpsol) and analyze the logs.

The
following linear program provides an example of ill conditioning
and round-off error in the input data:

$$
\begin{array}{rl}
\text{maximize} \\;\\;&x_1 + x_2 \\
\text{subject to} \\; \\; &\frac{1}{3}x_1 + \frac{2}{3}x_2 = 1\\
&x_1+2x_2=3 \\
&x_1,x_2 \geq 0.
\end{array}
$$

$$
\begin{array}{rl}
\text{maximize} \\;\\;&1\\
\text{subject to} \\; \\; &-x_1+24x_2\leq 21\\
&x_1\leq 3\\
&x_2 \geq 1.00000008.
\end{array}
$$




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

## Task 3 - Feature Selection

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




---
## Motivation

Linear regression was invented at the beginning of the 19th century and today,
after more than 200 years, it is still used extensively in practical
applications for description and prediction purposes:

- In econometrics, it is useful to estimate the price elasticity of a particular
  product by regressing sales revenue on price and possibly other features such
  as demographics and competitor and retail information.
- In health sciences, it can be applied to predict how long a patient will
  remain (i.e. length of stay) in the ER of a hospital based on patient
  information, triage assessment, medical test results, and the date/time of
  arrival.
- In social sciences, it may shed light on future academic performance of
  students, so proactive measures can be taken to improve their learning
  outcomes.

In general, linear regression is used to model the relationship between a
continuous variable and other explanatory variables, which can be either
continuous or categorical. When applying this technique, finding the subset of
features that maximizes its performance is often of interest.

---
## Problem Description

Linear regression is a supervised learning algorithm used to predict a
quantitative response. It assumes that there is a linear relationship between
the feature vector $x_i \in \mathbb{R}^d$ and the response $y_i \in \mathbb{R}$.
Mathematically speaking, for sample $i$ we have $y_i = \beta^T x_i +
\epsilon_i$, where $\beta \in \mathbb{R}^d$ is the vector of feature weights,
including the intercept, and  $\epsilon_i$ is a normally-distributed random
variable with zero mean and constant variance representing the error term. We
can learn the weights from a training dataset with $n$ observations $\{X \in
\mathbb{M}^{nxd},y \in \mathbb{R}^n\}$ by minimizing the Residual Sum of Squares
(RSS): $e^Te =(y-X\beta)^T (y-X\beta)=\beta^T X^T X\beta- 2y^TX\beta+y^T y$. The
Ordinary Least Squares (OLS) method achieves this by taking the derivative of
this quadratic and convex function and then finding the stationary point:
$\beta_{OLS}=(X^T X)^{-1} X^T y$.

In practice, some of the features are in fact not associated with the response. By including them, we only add unnecessary complexity to the model and increase variance to the weight estimates. However, finding the best performing model is no simple task as there is an exponential number of candidates, as one has to test $\sum_{s=1}^{d-1}{{d-1} \choose s}$ models. Since OLS rarely yields estimates that are exactly zero, thus discarding the features related to them, we need to resort to feature selection methods. Popular methods include:

- Subset selection, e.g. stepwise selection.
- Dimensionality reduction, e.g. principal component regression.
- Shrinkage, e.g. the Lasso.

The Lasso has undoubtedly been the method of choice for the last decade. Basically it fits a model containing all $d$ predictors, while incorporating a budget constraint based on the L1-norm of $\beta$, disregarding the intercept component. In fact, this method minimizes the RSS, subject to $\sum_{l=1}^{d-1}\mathopen|\beta_l\mathclose| \leq s$, where $s$ is a hyper-parameter representing the budget that is usually tuned via cross-validation. This constraint has the effect of shrinking all weight estimates, allowing some of them to be exactly zero when $s$ is small enough. Finally, it is worth noting that the unconstrained version of the Lasso is more frequently used. This version solves an unconstrained optimization problem where $RSS + \lambda \sum_{l=1}^{d-1}\mathopen|\beta_l\mathclose|$ is minimized, for a given value of the —modified— lagrangian multiplier $\lambda \in \mathbb{R}^+$.  

A similar formulation is now presented, where the L0-norm is used instead (although it is not really a proper norm). We now seek to minimize the RSS, subject to $\sum_{l=1}^{d-1}I(\beta_l \neq 0) \leq s$, where $I(\beta_l \neq 0)$ is an indicator function taking on the value of 1 if $\beta_j \neq 0$ and 0 otherwise. In this setting, $s$ represents the number of features to consider in the model. This optimization problem may be casted as a Mixed Integer Quadratic Program (MIQP). Traditionally, the feature selection problem has not been tackled this way because of the common belief in the statistics community that large-scale problems are intractable. But this is no longer the case, considering the computing power currently available and the performance of modern optimization solvers such as Gurobi.


Consider the [Feature Selection
case](https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/linear_regression/l0_regression.ipynb).

Implement the Lasso version together with minimizing the least absolute error.
Solve the linear programming problem and analyze the solution process in the
light of the article [KN1].

Implement the Lasso version (L1-norm as regularization component added to the
objective function) together with minimizing the least absolute error instead of
the square of residuals as done in the notebook. 

- Solve the linear programming problem in training and analyze the solution
  process in the light of the article [KN1]. 

- Compare the accuracy of the L1-norm and the L0-norm approach presented in the
  document.
